from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify({"Choo Choo": "НА ХУЙ ПА ШЕЛaaaaaa"})

@app.route('/aaa/')
def index():
    return jsonify({"Choo Choo": "НА ХУЙ ПА ШЕЛaaaaaa"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
