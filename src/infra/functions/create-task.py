from src.infra.factories.controllers.create_task import make_create_task_controller
import json


def handle(event, context):
    controller = make_create_task_controller()
    print(event)
    event_json = json.loads(json.dumps(event))
    body = json.loads(event_json['body'])
    try:
        controller.handle({"title": body['title']})
        response = {
            "statusCode": 201,
        }
        return response
    except Exception as error:
        response = {
            "statusCode": 500,
            "body": error
        }
        print(error)
        return response
