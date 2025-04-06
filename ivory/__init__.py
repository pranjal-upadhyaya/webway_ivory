"""Application factory for the Ivory frontend."""

import os
from flask import Flask, render_template, g
from injector import Injector

from ivory.views import register_blueprints
from ivory.constants.config import app_config
from ivory.modules import get_injector_instance, injector_instances

# Global injector instance
injector = injector_instances

def create_app():
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load config
    app.config.from_object(app_config)
    
    # Make injector available in request context
    @app.before_request
    def setup_injector():
        g.injector = injector
    
    # Register blueprints
    register_blueprints(app)
    
    # Register error handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("errors/500.html"), 500
    
    # Create a simple route to check if the app is running
    @app.route("/health")
    def health():
        return {"status": "ok"}
    
    # Add context processor for template variables
    @app.context_processor
    def inject_current_year():
        from datetime import datetime
        return {'current_year': datetime.now().year}
    
    # Add custom template filters
    @app.template_filter('current_year')
    def current_year_filter(text):
        from datetime import datetime
        return datetime.now().year
    
    return app 