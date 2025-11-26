"""
Type aliases for the research_assistant package.
"""

from typing import Any, Dict, List, Iterable, Callable, Tuple

# A generic configuration dictionary
ConfigDict = Dict[str, Any]

# A single record from a dataset, represented as a dictionary
DatasetRecord = Dict[str, Any]

# Representation for embeddings (e.g., vector of floats)
Embeddings = List[float]
