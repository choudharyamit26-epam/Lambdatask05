import os
from unittest.mock import Mock, patch
from tests.test_api_handler import ApiHandlerLambdaTestCase
from lambdas.api_handler.handler import HANDLER  # Ensure correct import

class TestSuccess(ApiHandlerLambdaTestCase):

    # @patch('lambdas.api_handler.handler.boto3.resource')  # Patch boto3.resource where used in handler
    # def test_success(self, mock_boto3_resource):
    #     # Set environment variables for AWS credentials
    #     os.environ['AWS_ACCESS_KEY_ID'] = 'ASIA5FTZDTP2F5RBJQYB'
    #     os.environ['AWS_SECRET_ACCESS_KEY'] = 'bQiI7C20kRBH8wWmOcLIDng1hTN6xpNCbAHvag1C'
    #     os.environ['AWS_SESSION_TOKEN'] = 'IQoJb3JpZ2luX2VjEJn//////////wEaCXVzLWVhc3QtMSJIMEYCIQCreywYXso0PCR1rsSk/uvI3LDwF2W9yhHsLD8uG037nQIhAOhFrhZ2WVe/AmCWKBYNMyUZ1ryAunGESyobOLeTJX3vKu0CCMH//////////wEQABoMOTA1NDE4MzQ5NTU2IgzmvzaI2s/UPbRcPVQqwQJh3NWuAkKhOYmK0G+brFQhEwp9SnxLONve9F4LAsdUV2ae9LnBj4aFaamdocZtFMpJ82u0FcTfpfUZ18ehLhyH/LcXxEBnhoSQE9uiMX9a2IQ8E/b1HxccgMUg6V06+xMjY3p1EAb1/R5IurMFDTFQTW6Voxel/gxbcMai5x5LFWRdMROuwcdWbiUey2xoSwWuXaYxntHECv/XViAp729B3F7ec0BTQEof5vkvM8w2hG8hiDwtHxIeVk+6F8EFq7CZNIUBWbYDd/6L7yOIPqN31fDQbjr5z+kQD7gmv+v01BeBN/9ZcuGUN82+cMGB/jOD/mIhrhN3HdqVKR0OtkbUDuMfJ0BSRDvHxaPield6+jYluxOCoIpogm3z61XDPnWcwcXMhJU4hR4hLOKpAGqgMALjH1vvIdIz3pL6LZEY4MUwsMmRtwY6nAGyytNT7PzPXO+bMxNSRr+2VityRSpGZsJnPMF6BKu347V4PWi9dCOlI3EHF9yhFjipYr96X6HvuymQK9/vMRHyF3HfkconnG+4mPFG74N05RVtlQZoAFFV2HiqDefF+vkn1Zzvqd43CfP8o3poKJu947/1RjVyTULg50KyUaLu8sG2HjnRLU0zj22JhUtzvH1E+JUmoWN7dcZS6OY='
    #
    #     # Mock the DynamoDB Table instance
    #     mock_table = Mock()
    #     mock_boto3_resource.return_value.Table.return_value = mock_table
    #     mock_table.put_item.return_value = {}  # Simulate successful put_item call
    #
    #     # Valid test input event
    #     test_event = {
    #         "principalId": 10,
    #         "content": {
    #             "param1": "value1",
    #             "param2": "value2"
    #         }
    #     }
    #
    #     # Mock Lambda context object with aws_request_id attribute
    #     test_context = Mock()
    #     test_context.aws_request_id = "test-unique-request-id"
    #
    #     # Expected result
    #     expected_response = {
    #         "statusCode": 201,
    #         "event": {
    #             "log_id": "test-unique-request-id",
    #             "principalId": 10,
    #             "content": {
    #                 "param1": "value1",
    #                 "param2": "value2"
    #             }
    #         }
    #     }
    #
    #     # Call the handler and check the result
    #     response = HANDLER.handle_request(test_event, test_context)
    #
    #     # Assert the result matches the expected output
    #     self.assertEqual(response, expected_response)

    @patch('lambdas.api_handler.handler.boto3.resource')  # Patch boto3.resource where used in handler
    def test_validation_error(self, mock_boto3_resource):
        # Set environment variables for AWS credentials
        os.environ['AWS_ACCESS_KEY_ID'] = 'ASIA5FTZDTP2F5RBJQYB'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'bQiI7C20kRBH8wWmOcLIDng1hTN6xpNCbAHvag1C'
        os.environ['AWS_SESSION_TOKEN'] = 'IQoJb3JpZ2luX2VjEJn//////////wEaCXVzLWVhc3QtMSJIMEYCIQCreywYXso0PCR1rsSk/uvI3LDwF2W9yhHsLD8uG037nQIhAOhFrhZ2WVe/AmCWKBYNMyUZ1ryAunGESyobOLeTJX3vKu0CCMH//////////wEQABoMOTA1NDE4MzQ5NTU2IgzmvzaI2s/UPbRcPVQqwQJh3NWuAkKhOYmK0G+brFQhEwp9SnxLONve9F4LAsdUV2ae9LnBj4aFaamdocZtFMpJ82u0FcTfpfUZ18ehLhyH/LcXxEBnhoSQE9uiMX9a2IQ8E/b1HxccgMUg6V06+xMjY3p1EAb1/R5IurMFDTFQTW6Voxel/gxbcMai5x5LFWRdMROuwcdWbiUey2xoSwWuXaYxntHECv/XViAp729B3F7ec0BTQEof5vkvM8w2hG8hiDwtHxIeVk+6F8EFq7CZNIUBWbYDd/6L7yOIPqN31fDQbjr5z+kQD7gmv+v01BeBN/9ZcuGUN82+cMGB/jOD/mIhrhN3HdqVKR0OtkbUDuMfJ0BSRDvHxaPield6+jYluxOCoIpogm3z61XDPnWcwcXMhJU4hR4hLOKpAGqgMALjH1vvIdIz3pL6LZEY4MUwsMmRtwY6nAGyytNT7PzPXO+bMxNSRr+2VityRSpGZsJnPMF6BKu347V4PWi9dCOlI3EHF9yhFjipYr96X6HvuymQK9/vMRHyF3HfkconnG+4mPFG74N05RVtlQZoAFFV2HiqDefF+vkn1Zzvqd43CfP8o3poKJu947/1RjVyTULg50KyUaLu8sG2HjnRLU0zj22JhUtzvH1E+JUmoWN7dcZS6OY='

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
        # Set environment variables for AWS credentials
        os.environ['AWS_ACCESS_KEY_ID'] = 'ASIA5FTZDTP2F5RBJQYB'
        os.environ['AWS_SECRET_ACCESS_KEY'] = 'bQiI7C20kRBH8wWmOcLIDng1hTN6xpNCbAHvag1C'
        os.environ['AWS_SESSION_TOKEN'] = 'IQoJb3JpZ2luX2VjEJn//////////wEaCXVzLWVhc3QtMSJIMEYCIQCreywYXso0PCR1rsSk/uvI3LDwF2W9yhHsLD8uG037nQIhAOhFrhZ2WVe/AmCWKBYNMyUZ1ryAunGESyobOLeTJX3vKu0CCMH//////////wEQABoMOTA1NDE4MzQ5NTU2IgzmvzaI2s/UPbRcPVQqwQJh3NWuAkKhOYmK0G+brFQhEwp9SnxLONve9F4LAsdUV2ae9LnBj4aFaamdocZtFMpJ82u0FcTfpfUZ18ehLhyH/LcXxEBnhoSQE9uiMX9a2IQ8E/b1HxccgMUg6V06+xMjY3p1EAb1/R5IurMFDTFQTW6Voxel/gxbcMai5x5LFWRdMROuwcdWbiUey2xoSwWuXaYxntHECv/XViAp729B3F7ec0BTQEof5vkvM8w2hG8hiDwtHxIeVk+6F8EFq7CZNIUBWbYDd/6L7yOIPqN31fDQbjr5z+kQD7gmv+v01BeBN/9ZcuGUN82+cMGB/jOD/mIhrhN3HdqVKR0OtkbUDuMfJ0BSRDvHxaPield6+jYluxOCoIpogm3z61XDPnWcwcXMhJU4hR4hLOKpAGqgMALjH1vvIdIz3pL6LZEY4MUwsMmRtwY6nAGyytNT7PzPXO+bMxNSRr+2VityRSpGZsJnPMF6BKu347V4PWi9dCOlI3EHF9yhFjipYr96X6HvuymQK9/vMRHyF3HfkconnG+4mPFG74N05RVtlQZoAFFV2HiqDefF+vkn1Zzvqd43CfP8o3poKJu947/1RjVyTULg50KyUaLu8sG2HjnRLU0zj22JhUtzvH1E+JUmoWN7dcZS6OY='

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
