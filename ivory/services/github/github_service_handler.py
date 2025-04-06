"""Implementation of GitHub service operations."""

from typing import Optional, List
from loguru import logger

from ivory.services.api_client import APIClient
from ivory.services.github.github_service import GitHubService
from ivory.models.github import Repository, RepositoryList
from ivory.constants.config import app_config


class GitHubServiceHandler(GitHubService):
    """Implementation of GitHub service operations."""
    api_client: APIClient
    
    def get_repositories(self) -> RepositoryList:
        """Get a list of GitHub repositories."""
        logger.debug(f"Fetching repositories from {app_config.ebony_base_url}")
        response = self.api_client.get(f"{app_config.ebony_base_url}/github/repos")
        logger.info(f"Retrieved {len(response)} repositories")
        logger.debug(f"GitHub repositories response: {response}")
        repositories = response.get("data", [])
        return RepositoryList.from_api_response(repositories)
    
    def get_repository(self, repo_name: str) -> Optional[Repository]:
        """Get a specific GitHub repository by name."""
        logger.debug(f"Looking for repository: {repo_name}")
        repositories = self.get_repositories()
        for repo in repositories.repositories:
            if repo.name == repo_name:
                logger.info(f"Found repository: {repo_name}")
                return repo
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
        return RepositoryList(repositories=matching_repos)
    
    def get_repository_languages(self, repo_name: str) -> List[str]:
        """Get the languages used in a specific GitHub repository."""
        repo = self.get_repository(repo_name)
        return repo.languages if repo else []
