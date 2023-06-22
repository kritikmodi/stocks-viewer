from flask import Flask, request
import sys
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return "Hello World Service!"

def __service_main__(port):
    app.run('0.0.0.0', port=int(port), debug=False)

@app.route('/function/<x>/<y>', methods=['GET'])
def function_a(x, y):
    '''
    requests.get('http://localhost:1024/function/1/2').content
    '''
    return f"function({x=}, {y=})"

@app.route('/function', methods=['GET'])
def function_b():
    '''
    requests.get('http://localhost:1024/function', params={'x': 1, 'y': 2}).content
    '''
    x = request.args.get('x')
    y = request.args.get('y')
    return f"function({x=}, {y=})"

if __name__ == '__main__':
    __service_main__(1024)
