from src.infra.factories.controllers.list_tasks import make_list_tasks_controller
import json


def handle(event, context):
    controller = make_list_tasks_controller()
    try:
        tasks = controller.handle()
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
