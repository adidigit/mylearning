"""
Custom exceptions for the research_assistant package.
"""


class DataLoadError(Exception):
    """Raised when there is an error loading data."""
    pass


class RetrievalError(Exception):
    """Raised when retrieval pipeline fails."""
    pass


class InferenceError(Exception):
    """Raised when inference engine encounters an error."""
    pass


class ConfigurationError(Exception):
    """Raised when configuration is invalid or missing required fields."""
    pass
