from flask import Flask, request, jsonify

from main import process1, process2


app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome'})

# TODO: Create a flask app with two routes, one for each function.
# The route should get the data from the request, call the function, and return the result.

# Route for process1
@app.route('/process1', methods=['POST'])
def process1_route():
    data = request.json
    result = process1(data)
    return result

# Route for process2
@app.route('/process2', methods=['POST'])
def process2_route():
    data = request.json
    result = process2(data)
    return result

if __name__ == '__main__':
    app.run(port=5000, debug=True)