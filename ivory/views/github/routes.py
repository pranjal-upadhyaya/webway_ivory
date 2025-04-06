"""Routes for GitHub-related views."""

from flask import render_template, current_app, request, g

from . import github_bp
from ivory.services.github import GitHubService
from ivory.models.github.repository import LANGUAGE_COLORS


@github_bp.route("/repos")
def repos():
    """Display a list of GitHub repositories."""
    try:
        # Get the service from the injector
        github_service = g.injector.get(GitHubService)
        
        # Check if there's a search query
        search_query = request.args.get('q', '').strip()
        
        if search_query:
            # Get repositories matching the search query
            repository_list = github_service.search_repositories(search_query)
        else:
            # Get all repositories
            repository_list = github_service.get_repositories()
        
        # Pass repositories to the template
        return render_template(
            "github/repos.html",
            repositories=repository_list.repositories,
            language_colors=LANGUAGE_COLORS,
            search_query=search_query,
            error=None
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching GitHub repositories: {str(e)}")
        return render_template(
            "github/repos.html",
            repositories=[],
            language_colors=LANGUAGE_COLORS,
            search_query=request.args.get('q', ''),
            error="Unable to fetch GitHub repositories at this time."
        )


@github_bp.route("/repos/<repo_name>")
def repo_detail(repo_name):
    """Display details for a specific GitHub repository."""
    try:
        # Get the service from the injector
        github_service = g.injector.get(GitHubService)
        
        # Get the specific repository
        repository = github_service.get_repository(repo_name)
        
        if not repository:
            return render_template(
                "github/repo_detail.html",
                repository=None,
                language_colors=LANGUAGE_COLORS,
                error=f"Repository '{repo_name}' not found."
            )
        
        # Pass repository to the template
        return render_template(
            "github/repo_detail.html",
            repository=repository,
            language_colors=LANGUAGE_COLORS,
            error=None
        )
    except Exception as e:
        current_app.logger.error(f"Error fetching GitHub repository '{repo_name}': {str(e)}")
        return render_template(
            "github/repo_detail.html",
            repository=None,
            language_colors=LANGUAGE_COLORS,
            error=f"Unable to fetch GitHub repository '{repo_name}' at this time."
        )