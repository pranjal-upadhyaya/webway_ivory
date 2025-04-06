"""Logging configuration for the application."""

import logging
import sys
from flask import Flask
from loguru import logger


def configure_logging(app: Flask, log_level: str = "INFO") -> None:
    """Configure logging for the application.
    
    Args:
        app: The Flask application
        log_level: The log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Remove default loguru handler
    logger.remove()
    
    # Add a new handler for loguru that outputs to stderr
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=log_level,
        colorize=True,
    )
    
    # Intercept Flask's logger
    class InterceptHandler(logging.Handler):
        def emit(self, record):
            # Get corresponding Loguru level if it exists
            try:
                level = logger.level(record.levelname).name
            except ValueError:
                level = record.levelno

            # Find caller from where originated the logged message
            frame, depth = logging.currentframe(), 2
            while frame.f_code.co_filename == logging.__file__:
                frame = frame.f_back
                depth += 1

            logger.opt(depth=depth, exception=record.exc_info).log(
                level, record.getMessage()
            )

    # Configure Flask logger to use our handler
    logging.basicConfig(handlers=[InterceptHandler()], level=0, force=True)
    
    # Replace Flask's logger
    app.logger.handlers = []
    app.logger.propagate = True
    
    # Set log level for all loggers
    logging.getLogger().setLevel(logging.getLevelName(log_level))
    logger.info(f"Logging configured at level {log_level}") 