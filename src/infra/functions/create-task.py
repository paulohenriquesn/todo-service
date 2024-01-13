from src.infra.factories.controllers.create_task import make_create_task_controller
import json


def handle(event, context):
    controller = make_create_task_controller()
    try:
        controller.handle({"title": "test"})
        response = {
            "statusCode": 201,
            "body": json.dumps(event)
        }
        return response
    except Exception as error:
        response = {
            "statusCode": 500,
            "body": json.dumps(error)
        }
        return response
