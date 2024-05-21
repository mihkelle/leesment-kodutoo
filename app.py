from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

server_ip = "4.211.158.21"
server_port = 80


@app.route("/health")
def health():
    return "OK"


@app.route("/")
def index():
    try:
        response = requests.get(f"http://{server_ip}:{server_port}")
        response.raise_for_status()
        app.logger.info(f"Successfully fetched data from VM: {response.text}")
        return response.text
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching data from VM: {str(e)}")
        return str(e), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
