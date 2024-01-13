from src.app.factories.controllers.create_task import make_create_task_controller
from src.app.proxy_request import proxy_request


def handle(event, context):
    controller = make_create_task_controller()
    try:
        proxy_request(controller, event)
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
