import json
from src.app.factories.controllers.list_tasks import make_list_tasks_controller
from src.app.proxy_request import proxy_request


def handle(event, context):
    controller = make_list_tasks_controller()
    try:
        tasks = proxy_request(controller, event)
        response = {
            "statusCode": 200,
            "body": json.dumps(tasks, default=lambda x: x.__dict__)
        }
        return response
    except Exception as error:
        response = {
            "statusCode": 500,
            "body": error
        }
        print(error)
        return response
