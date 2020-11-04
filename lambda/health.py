import json

def handler(event, context):
    message = 'OK'
    
    return {
        "statusCode": 200,
        "body": json.dumps(message)
    }
