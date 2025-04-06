"""Implementation of GitHub service operations."""

from ebony.models.github.github_models import GetGithubRepositoriesResponse

from typing import Optional, List
from loguru import logger

from ivory.services.api_client import APIClient
from ivory.services.github.github_service import GitHubService
from ivory.models.github import Repository, RepositoryList
from ivory.constants.config import app_config


class GitHubServiceHandler(GitHubService):
    """Implementation of GitHub service operations."""
    api_client: APIClient
    
    def get_repositories(self) -> GetGithubRepositoriesResponse:
        """Get a list of GitHub repositories."""
        logger.debug(f"Fetching repositories from {app_config.ebony_base_url}")
        ebony_response = self.api_client.get(f"{app_config.ebony_base_url}/github/repos")
        logger.info(f"Retrieved {len(ebony_response)} repositories")
        response_data = ebony_response["data"]
        return GetGithubRepositoriesResponse(**response_data)
    
    def get_repository(self, repo_name: str) -> Optional[Repository]:
        """Get a specific GitHub repository by name."""
        logger.debug(f"Looking for repository: {repo_name}")
        repositories = self.get_repositories()
        for repository in repositories.repositories:
            if repository.name == repo_name:
                logger.info(f"Found repository: {repo_name}")
                return repository
        logger.warning(f"Repository not found: {repo_name}")
        return None
        
    def search_repositories(self, query: str) -> RepositoryList:
        """Search for GitHub repositories by query."""
        logger.debug(f"Searching repositories with query: {query}")
        # In a real implementation, this would make a call to an API search endpoint
        # For now, we'll just filter the repositories we already have
        all_repos = self.get_repositories()
        matching_repos = [
            repo for repo in all_repos.repositories
            if query.lower() in repo.name.lower() or 
               (repo.description and query.lower() in repo.description.lower())
        ]
        logger.info(f"Found {len(matching_repos)} repositories matching query: {query}")
        return GetGithubRepositoriesResponse(repositories = matching_repos)
    
    def get_repository_languages(self, repo_name: str) -> List[str]:
        """Get the languages used in a specific GitHub repository."""
        repo = self.get_repository(repo_name)
        return repo.languages if repo else []
