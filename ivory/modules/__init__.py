"""Configuration modules for dependency injection."""

from injector import Injector, Module, singleton, provider

from ivory.modules.github_module import GitHubModule
from ivory.services.api_client import APIClient
from ivory.services.github.github_service import GitHubService
from ivory.services.github.github_service_handler import GitHubServiceHandler


modules = [GitHubModule()]

injector_instances = Injector(modules)


def get_injector_instance(service: type):
    return injector_instances.get(service)