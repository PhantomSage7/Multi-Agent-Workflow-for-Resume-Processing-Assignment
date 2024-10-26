# agents/__init__.py

# Import the necessary function(s) from the graph module
from .graph import create_workflow

# Define what is available for import when using 'from agents import *'
__all__ = ['create_workflow']

# # Optional: Initialize logging for the package
# import logging

# # Configure logging for the package
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Log that the package has been initialized
# logger.info("Agents package initialized.")