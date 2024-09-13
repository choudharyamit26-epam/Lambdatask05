from unittest.mock import Mock, patch

from tests.test_api_handler import ApiHandlerLambdaTestCase

from lambdas.api_handler.handler import HANDLER  # Ensure correct import


class TestSuccess(ApiHandlerLambdaTestCase):

    @patch('lambdas.api_handler.handler.boto3.resource')  # Patch boto3.resource where used in handler
    def test_validation_error(self, mock_boto3_resource):
        # Mock the DynamoDB Table instance
        mock_table = Mock()
        mock_boto3_resource.return_value.Table.return_value = mock_table
        mock_table.put_item.return_value = {}

        # Invalid test input event (missing 'principalId')
        test_event = {
            "content": {
                "param1": "value1",
                "param2": "value2"
            }
        }

        # Mock Lambda context object with aws_request_id attribute
        test_context = Mock()
        test_context.aws_request_id = "test-unique-request-id"

        # Expected result
        expected_response = {
            "statusCode": 400,
            "errorMessage": "Invalid request format. 'principalId' and 'content' are required."
        }

        # Call the handler and check the result
        response = HANDLER.handle_request(test_event, test_context)

        # Assert the result matches the expected output
        self.assertEqual(response, expected_response)

    @patch('lambdas.api_handler.handler.boto3.resource')  # Patch boto3.resource where used in handler
    def test_internal_server_error(self, mock_boto3_resource):
        # Mock the DynamoDB Table instance
        mock_table = Mock()
        mock_boto3_resource.return_value.Table.return_value = mock_table
        # Simulate an exception when calling put_item
        mock_table.put_item.side_effect = Exception("Unable to locate credentials")

        # Valid test input event
        test_event = {
            "principalId": 10,
            "content": {
                "param1": "value1",
                "param2": "value2"
            }
        }

        # Mock Lambda context object with aws_request_id attribute
        test_context = Mock()
        test_context.aws_request_id = "test-unique-request-id"

        # Expected result
        expected_response = {
            "statusCode": 500,
            "errorMessage": "Internal server error",
            "details": "Unable to locate credentials"
        }

        # Call the handler and check the result
        response = HANDLER.handle_request(test_event, test_context)

        # Assert the result matches the expected output
        self.assertEqual(response, expected_response)
