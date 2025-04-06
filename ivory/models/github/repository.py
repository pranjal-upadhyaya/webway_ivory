"""GitHub repository models."""

from typing import List, Dict, Optional
from pydantic import BaseModel, Field


class Repository(BaseModel):
    """GitHub repository model."""
    
    id: int
    name: str
    full_name: str
    html_url: str
    description: Optional[str] = None
    language: Optional[str] = None
    stars: int = Field(0, alias="stargazers_count")
    forks: int = Field(0, alias="forks_count")
    is_private: bool = Field(False, alias="private")
    updated_at: str
    created_at: str


class RepositoryList(BaseModel):
    """A list of GitHub repositories."""
    
    repositories: List[Repository]
    
    @classmethod
    def from_api_response(cls, data: List[Dict]) -> "RepositoryList":
        """Create a RepositoryList from the API response."""
        repos = [Repository(**repo) for repo in data]
        return cls(repositories=repos)


# Common language colors for display purposes
LANGUAGE_COLORS = {
    "Python": "#3572A5",
    "JavaScript": "#f1e05a",
    "TypeScript": "#2b7489",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Java": "#b07219",
    "C++": "#f34b7d",
    "C#": "#178600",
    "Go": "#00ADD8",
    "Ruby": "#701516",
    "PHP": "#4F5D95",
    "Swift": "#ffac45",
    "Kotlin": "#F18E33",
    "Rust": "#dea584",
} 