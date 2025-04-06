"""GitHub views package."""

from flask import Blueprint

# Create the GitHub blueprint
github_bp = Blueprint("github", __name__, url_prefix="/github")

# Import routes after blueprint creation to avoid circular imports
from . import routes 