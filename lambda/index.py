import os
import json
import boto3
import uuid

def handler(event, context):
    region = os.environ.get('AWS_REGION')
    table = os.environ.get('table')
    dynamodb = boto3.client('dynamodb')

    message = 'This is a hello from {}!'.format(region)  
    
    dynamodb.put_item(TableName=table,
            Item={
                'id':{'S': str(uuid.uuid4())},
                'message':{'S':message}
                }
            )

    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }
