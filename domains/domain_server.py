import json, redis
from flask import Flask, jsonify, request

redis = redis.StrictRedis()

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
    return json.dumps({"message" : "ok"})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8022)
