"""Routes for GitHub-related views."""

from flask import render_template, current_app, request, g
from loguru import logger

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
        
        logger.debug(f"GitHub repos route accessed, search query: '{search_query}'")
        
        if search_query:
            # Get repositories matching the search query
            repository_list = github_service.search_repositories(search_query)
        else:
            # Get all repositories
            repository_list = github_service.get_repositories()
        
        logger.info(f"Rendering GitHub repos template with {len(repository_list.repositories)} repositories")
        
        # Pass repositories to the template
        return render_template(
            "github/repos.html",
            repositories=repository_list.repositories,
            language_colors=LANGUAGE_COLORS,
            search_query=search_query,
            error=None
        )
    except Exception as e:
        logger.error(f"Error fetching GitHub repositories: {str(e)}", exc_info=True)
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
        logger.debug(f"GitHub repo detail route accessed for repo: {repo_name}")
        
        # Get the service from the injector
        github_service = g.injector.get(GitHubService)
        
        # Get the specific repository
        repository = github_service.get_repository(repo_name)
        
        if not repository:
            logger.warning(f"Repository not found: {repo_name}")
            return render_template(
                "github/repo_detail.html",
                repository=None,
                language_colors=LANGUAGE_COLORS,
                error=f"Repository '{repo_name}' not found."
            )
        
        logger.info(f"Rendering GitHub repo detail template for: {repo_name}")
        
        # Pass repository to the template
        return render_template(
            "github/repo_detail.html",
            repository=repository,
            language_colors=LANGUAGE_COLORS,
            error=None
        )
    except Exception as e:
        logger.error(f"Error fetching GitHub repository '{repo_name}': {str(e)}", exc_info=True)
        return render_template(
            "github/repo_detail.html",
            repository=None,
            language_colors=LANGUAGE_COLORS,
            error=f"Unable to fetch GitHub repository '{repo_name}' at this time."
        )