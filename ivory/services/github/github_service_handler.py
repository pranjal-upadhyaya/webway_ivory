"""Implementation of GitHub service operations."""

from typing import Optional, List

from ivory.services.api_client import APIClient
from ivory.services.github.github_service import GitHubService
from ivory.models.github import Repository, RepositoryList


class GitHubServiceHandler(GitHubService):
    """Implementation of GitHub service operations."""
    api_client: APIClient
    
    # def __init__(self, api_client: APIClient):
    #     """Initialize the service with an API client.
        
    #     Args:
    #         api_client: API client for making requests to the backend
    #     """
    #     self.api_client = api_client
    
    def get_repositories(self) -> RepositoryList:
        """Get a list of GitHub repositories."""
        response = self.api_client.get("github/repos")
        repositories = response.get("data", [])
        return RepositoryList.from_api_response(repositories)
    
    def get_repository(self, repo_name: str) -> Optional[Repository]:
        """Get a specific GitHub repository by name."""
        repositories = self.get_repositories()
        for repo in repositories.repositories:
            if repo.name == repo_name:
                return repo
        return None
        
    def search_repositories(self, query: str) -> RepositoryList:
        """Search for GitHub repositories by query."""
        # In a real implementation, this would make a call to an API search endpoint
        # For now, we'll just filter the repositories we already have
        all_repos = self.get_repositories()
        matching_repos = [
            repo for repo in all_repos.repositories 
            if query.lower() in repo.name.lower() or 
               (repo.description and query.lower() in repo.description.lower())
        ]
        return RepositoryList(repositories=matching_repos)
    
    def get_repository_languages(self, repo_name: str) -> List[str]:
        """Get the languages used in a specific GitHub repository."""
        repo = self.get_repository(repo_name)
        return repo.languages if repo else []
