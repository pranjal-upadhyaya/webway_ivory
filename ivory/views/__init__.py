"""Views package for route handling."""

from flask import Blueprint, render_template
from ivory.views.github import github_bp

# Create a main blueprint for the index page
main = Blueprint("views", __name__, url_prefix="/")

@main.route("/")
def index():
    """Render the index page."""
    return render_template("index.html")

# Import and register all domain blueprints
def register_blueprints(app):
    """Register all blueprints with the application."""
    app.register_blueprint(main)
    app.register_blueprint(github_bp)
    
    # Other blueprints will be registered here as they are developed
    # app.register_blueprint(user_bp)
    # app.register_blueprint(project_bp)
    # app.register_blueprint(auth_bp) 