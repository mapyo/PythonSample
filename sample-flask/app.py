from flask import Flask, jsonify, make_response

app = Flask(__name__)


@app.route('/tasks', methods=['GET'])
def index():
    tasks = [
        {
            "id": 10,
            "name": "aaaa"
        }
    ]
    return make_response(jsonify({"tasks": tasks}))


if __name__ == "__main__":
    app.run(debug=True)
