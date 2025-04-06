"""Entry point for the Ivory frontend application."""

from ivory import create_app
from ivory.constants.config import app_config
app = create_app()

if __name__ == "__main__":
    app.run(
        debug=True, 
        host=app_config.app_host, 
        port=app_config.app_port,
        threaded=True
        )
