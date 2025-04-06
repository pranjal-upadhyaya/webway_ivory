"""Base API client for communicating with the backend."""

import json
from typing import Any, Dict, Optional, Union

import flask


class APIError(Exception):
    """Exception raised for API errors."""
    
    def __init__(self, status_code: int, message: str):
        self.status_code = status_code
        self.message = message
        super().__init__(f"API Error ({status_code}): {message}")


class APIClient:
    """Base API client for communicating with the backend."""
    
    def __init__(self, base_url: str = None):
        """Initialize the API client with a base URL."""
        # This is a dummy URL for development; it will be configured properly later
        self.base_url = base_url or "http://localhost:5000/api/v1"
    
    def _get_headers(self) -> Dict[str, str]:
        """Get the headers for the API request."""
        headers = {
            "Content-Type": "application/json",
        }
        
        # Add authentication token if available in session
        # if flask.has_request_context() and "auth_token" in flask.session:
        #     headers["Authorization"] = f"Bearer {flask.session['auth_token']}"
        
        return headers
    
    def _handle_response(self, response) -> Dict:
        """Handle the API response."""
        if response.status_code >= 400:
            try:
                error_data = response.json()
                message = error_data.get("message", "Unknown error")
            except json.JSONDecodeError:
                message = response.text or "Unknown error"
            
            raise APIError(response.status_code, message)
        
        try:
            return response.json()
        except json.JSONDecodeError:
            return {"message": "No content"}
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict:
        """Make a GET request to the API."""
        # For development, return mock data
        # In production, this would make a real HTTP request
        if "github/repos" in endpoint:
            return self._mock_github_repos()
        
        # This is a placeholder for actual HTTP requests
        # In a real implementation, we would use requests library
        # response = requests.get(
        #     f"{self.base_url}/{endpoint.lstrip('/')}",
        #     params=params,
        #     headers=self._get_headers(),
        # )
        # return self._handle_response(response)
        
        return {"message": "Mock API response"}
    
    def post(self, endpoint: str, data: Dict[str, Any]) -> Dict:
        """Make a POST request to the API."""
        # Placeholder for actual HTTP requests
        return {"message": "Mock API response"}
    
    def put(self, endpoint: str, data: Dict[str, Any]) -> Dict:
        """Make a PUT request to the API."""
        # Placeholder for actual HTTP requests
        return {"message": "Mock API response"}
    
    def delete(self, endpoint: str) -> Dict:
        """Make a DELETE request to the API."""
        # Placeholder for actual HTTP requests
        return {"message": "Mock API response"}
    
    def _mock_github_repos(self) -> Dict:
        """Return mock GitHub repository data for development."""
        return {
            "data": [
                {
                    "id": 1,
                    "name": "webway-ivory",
                    "full_name": "username/webway-ivory",
                    "html_url": "https://github.com/username/webway-ivory",
                    "description": "Frontend for the Webway application",
                    "language": "Python",
                    "stargazers_count": 15,
                    "forks_count": 3,
                    "private": False,
                    "updated_at": "2023-04-01T12:00:00Z",
                    "created_at": "2023-01-15T10:00:00Z"
                },
                {
                    "id": 2,
                    "name": "webway-ebony",
                    "full_name": "username/webway-ebony",
                    "html_url": "https://github.com/username/webway-ebony",
                    "description": "Backend API for the Webway application",
                    "language": "Python",
                    "stargazers_count": 12,
                    "forks_count": 2,
                    "private": False,
                    "updated_at": "2023-04-02T14:30:00Z",
                    "created_at": "2023-01-15T10:00:00Z"
                },
                {
                    "id": 3,
                    "name": "personal-website",
                    "full_name": "username/personal-website",
                    "html_url": "https://github.com/username/personal-website",
                    "description": "My personal portfolio website",
                    "language": "JavaScript",
                    "stargazers_count": 8,
                    "forks_count": 1,
                    "private": False,
                    "updated_at": "2023-03-20T09:15:00Z",
                    "created_at": "2022-10-05T16:45:00Z"
                },
                {
                    "id": 4,
                    "name": "data-visualization-toolkit",
                    "full_name": "username/data-visualization-toolkit",
                    "html_url": "https://github.com/username/data-visualization-toolkit",
                    "description": "A toolkit for data visualization in web applications",
                    "language": "TypeScript",
                    "stargazers_count": 32,
                    "forks_count": 7,
                    "private": False,
                    "updated_at": "2023-04-05T11:20:00Z",
                    "created_at": "2022-06-18T14:20:00Z"
                }
            ]
        } 