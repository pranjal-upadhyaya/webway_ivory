from ivory.constants.config import app_config

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"


if __name__ == "__main__":
    app.run(
        host=app_config.app_host,
        port=app_config.app_port,
        debug=True
    )
