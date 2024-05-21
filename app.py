from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

server_ip = "4.211.158.21"
server_port = 80


@app.route("/")
def index():
    try:
        response = requests.get(f"http://{server_ip}:{server_port}")
        return response.text
    except requests.exceptions.RequestException as e:
        return str(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
