import boto3

from commons.abstract_lambda import AbstractLambda
from commons.log_helper import get_logger

_LOG = get_logger('ApiHandler-handler')

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')
table = dynamodb.Table('Events')


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        """
        Validate the incoming event. This can be enhanced for proper validation.
        """
        if 'principalId' not in event or 'content' not in event:
            raise ValueError("Invalid request format. 'principalId' and 'content' are required.")

        if not isinstance(event['principalId'], int):
            raise ValueError("Invalid 'principalId'. It should be an integer.")

        if not isinstance(event['content'], dict):
            raise ValueError("Invalid 'content'. It should be a dictionary.")

        return event  # Return the validated event

    def handle_request(self, event, context):
        """
        Handle incoming event, store it in DynamoDB, and return the created event.
        """
        try:
            # Validate the incoming request
            valid_event = self.validate_request(event)

            # Prepare the item to put in DynamoDB
            item = {
                'log_id': str(context.aws_request_id),  # Unique ID based on the Lambda context
                'principalId': valid_event['principalId'],
                'content': valid_event['content']
            }

            # Insert the item into the DynamoDB table
            table.put_item(Item=item)

            # Log the successful operation
            _LOG.info(f"Successfully stored item in DynamoDB: {item}")

            # Return a success response with the created event
            response = {
                'statusCode': 201,
                'event': item
            }
            return response

        except ValueError as e:
            # Log the validation error
            _LOG.error(f"Validation error: {str(e)}")
            # Return 400 response for validation errors
            return {
                'statusCode': 400,
                'errorMessage': str(e)
            }

        except Exception as e:
            # Log the internal server error
            _LOG.error(f"Internal server error: {str(e)}")
            # Return 500 response for any other errors
            return {
                'statusCode': 500,
                'errorMessage': "Internal server error",
                'details': str(e)
            }


HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.handle_request(event=event, context=context)
