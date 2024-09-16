import os
import traceback
import uuid
from datetime import datetime

import boto3

from commons.abstract_lambda import AbstractLambda
from commons.log_helper import get_logger

_LOG = get_logger('ApiHandler-handler')

# DynamoDB setup
dynamodb = boto3.resource('dynamodb', region_name='eu-central-1')


# table_name = 'Events'  # Ensure this matches your table name exactly
# table = dynamodb.Table(table_name)
# print("-----------", table)


class ApiHandler(AbstractLambda):

    def validate_request(self, event) -> dict:
        if 'principalId' not in event or 'content' not in event:
            raise ValueError("Invalid request format. 'principalId' and 'content' are required.")

        if not isinstance(event['principalId'], int):
            raise ValueError("Invalid 'principalId'. It should be an integer.")

        if not isinstance(event['content'], dict):
            raise ValueError("Invalid 'content'. It should be a dictionary.")

        return event

    def handle_request(self, event, context):
        table = os.environ.get("table_name")
        print("-----------", table)

        try:
            valid_event = self.validate_request(event)
            item = {
                'id': str(uuid.uuid4()),
                'principalId': valid_event['principalId'],
                'body': valid_event['content'],
                'createdAt': datetime.utcnow().isoformat() + 'Z'
            }

            try:
                table_data = table.put_item(Item=item)
                print("---------- INSERTED ITEM IN TABLE", table_data, event, item)
            except Exception as e:
                _LOG.error(f"Failed to store item in DynamoDB table {table}: {item}")
                _LOG.error(f"DynamoDB error: {str(e)}")
                return {
                    'statusCode': 500,
                    'errorMessage': "Internal server error while storing data.",
                    'details': str(e),
                    'traceback': traceback.format_exc()
                }

            _LOG.info(f"Successfully stored item in DynamoDB table {table}: {item}")

            response = {
                'statusCode': 201,
                'event': item
            }
            return response

        except Exception as e:
            _LOG.error(f"Internal server error: {str(e)}")
            return {
                'statusCode': 500,
                'error': {
                    'message': "Internal server error",
                    'details': str(e),
                    'traceback': traceback.format_exc()
                }
            }


HANDLER = ApiHandler()


def lambda_handler(event, context):
    return HANDLER.handle_request(event=event, context=context)
