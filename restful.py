from pickle import FALSE, TRUE
from flask import Flask, jsonify, request
app = Flask(__name__)

numbers = [{'first' : 0, 'second' : 0},]

@app.route('/', methods=['GET'])
def test():
    return jsonify({'message' : 'It works'})


@app.route('/num', methods=['GET'])
def returnAll():
    return jsonify({ 'numbers' : numbers})

@app.route('/num', methods=['POST'])
def updateNumbers():
    newNumbers = {"first" : request.json["first"], "second" : request.json["second"]}
    numbers.clear()
    numbers.append(newNumbers)
    return jsonify({'numbers' : numbers})


if __name__ == "__main__":
    app.run(debug=FALSE, port=8000)