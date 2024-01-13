import json


def handle(event, context):
    body = {
        "message": "task created",
        "input": event
    }

    response = {
        "statusCode": 201,
        "body": json.dumps(body)
    }

    return response
