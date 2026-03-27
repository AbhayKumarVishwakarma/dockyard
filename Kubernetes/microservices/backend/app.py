from flask import Flask, jsonify
from connections import coll
import os

app = Flask(__name__)

PORT = os.environ.get('PORT', 8000)


@app.route('/')
def home():
    return jsonify({"message": "Backend is up and running!"})


@app.route('/api/names', methods=['GET'])
def get_names():

    names = coll.find()
    
    arr = []
    for name in names:
        arr.append(name['value'])

    result = {
        "data": arr
    }

    return jsonify(result)


@app.route('/api/add/<name>')
def add_name(name):

    coll.insert_one({"value": name})

    return jsonify({"message": f"{name} added successfully!"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=True)