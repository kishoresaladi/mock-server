from flask import Flask, request
import os
import json

app = Flask(__name__)
filename = os.environ.get('mock-file-data')
with open(filename, 'r') as f:
    url_output_map = json.load(f)

def base_response_to_request():
    key = "/" + request.base_url.lstrip(request.host_url)
    output_list = url_output_map[key].get(request.method)
    for output in output_list:
        if all(output['query_string'].get(arg)== request.args.get(arg) for arg in request.args):
            return output.get('response')
    return 'HI"'


def bootstrap(app):
    for url in url_output_map:
        app.add_url_rule(url, url, base_response_to_request)

bootstrap(app)

