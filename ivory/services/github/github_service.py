"""Service interface for GitHub operations."""

from abc import ABC, abstractmethod
from typing import List, Optional

from ivory.models.github import Repository, RepositoryList


class GitHubService(ABC):
    """Abstract service interface for GitHub operations."""
    
    @abstractmethod
    def get_repositories(self) -> RepositoryList:
        """Get a list of GitHub repositories."""
        pass
    
    @abstractmethod
    def get_repository(self, repo_name: str) -> Optional[Repository]:
        """Get a specific GitHub repository by name."""
        pass
        
    @abstractmethod
    def search_repositories(self, query: str) -> RepositoryList:
        """Search for GitHub repositories by query."""
        pass
    
    @abstractmethod
    def get_repository_languages(self, repo_name: str) -> List[str]:
        """Get the languages used in a specific GitHub repository."""
        pass
    