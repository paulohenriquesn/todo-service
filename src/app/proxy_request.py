import json


def proxy_request(controller, event):
    event_json = json.loads(json.dumps(event))
    body = None
    if event_json['body']:
        body = json.loads(event_json['body'])
        print(body)
    return controller.handle(body)
