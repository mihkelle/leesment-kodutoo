import logging
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

server_ip = "4.211.158.21"
server_port = 80

# Seadistage logimise tase ja formaat
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)


@app.route("/health")
def health():
    app.logger.debug("Health endpoint accessed")
    return "OK"


@app.route("/")
def index():
    app.logger.debug("Index endpoint accessed")
    try:
        response = requests.get(f"http://{server_ip}:{server_port}")
        response.raise_for_status()
        app.logger.info(f"Successfully fetched data from VM: {response.text}")
        return response.text
    except requests.exceptions.RequestException as e:
        app.logger.error(f"Error fetching data from VM: {str(e)}")
        return str(e), 500


if __name__ == "__main__":
    app.logger.debug("Starting Flask app")
    app.run(host="0.0.0.0", port=8000)
