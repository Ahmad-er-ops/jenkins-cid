# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Route for addition
@app.route('/add')
def add_route():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({"result": add(a, b)})

# Route for subtraction
@app.route('/subtract')
def subtract_route():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    return jsonify({"result": subtract(a, b)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
