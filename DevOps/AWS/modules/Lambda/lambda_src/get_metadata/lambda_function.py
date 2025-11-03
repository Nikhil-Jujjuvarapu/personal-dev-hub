import boto3
import json
from decimal import Decimal

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ImageMetadata')  # Replace with your table name

def decimal_to_native(obj):
    if isinstance(obj, list):
        return [decimal_to_native(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: decimal_to_native(v) for k, v in obj.items()}
    elif isinstance(obj, Decimal):
        return int(obj) if obj % 1 == 0 else float(obj)
    else:
        return obj

def lambda_handler(event, context):
    try:
        # Safely extract file_name from query parameters
        qs = event.get('queryStringParameters') or {}
        file_name = qs.get('file_name')

        if not file_name:
            return {
                "statusCode": 400,
                "body": json.dumps({"error": "Missing file_name parameter"})
            }

        # Fetch item from DynamoDB
        response = table.get_item(Key={'file_name': file_name})

        if 'Item' not in response:
            return {
                "statusCode": 404,
                "body": json.dumps({"error": f"No metadata found for {file_name}"})
            }

        item = decimal_to_native(response['Item'])

        return {
            "statusCode": 200,
            "body": json.dumps(item)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
