from injector import Module, inject, provider, singleton

from ivory.services.api_client import APIClient
from ivory.services.github.github_service import GitHubService
from ivory.services.github.github_service_handler import GitHubServiceHandler


class GitHubModule(Module):
    """Module for GitHub-related bindings."""
    
    @provider
    @singleton
    def provide_github_service(self, api_client: APIClient) -> GitHubService:
        """Provide a GitHub service implementation.
        
        Args:
            api_client: Injected API client
            
        Returns:
            A GitHubServiceHandler instance that implements GitHubService
        """
        handler = GitHubServiceHandler()
        handler.api_client = api_client  # Manually set the field
        return handler
