"""
Dataset loader utilities.

This module defines functions to load datasets from local files or
external sources such as the HuggingFace hub. It is intentionally
minimal; teams should expand it to handle their specific formats.
"""
from __future__ import annotations

from typing import Any

import pandas as pd
from datasets import load_dataset as hf_load_dataset


def load_dataset(name: str, split: str = "train") -> Any:
    """Load a dataset by name using the `datasets` library.

    Args:
        name: The name of the dataset on HuggingFace (e.g. "squad").
        split: The dataset split (e.g. "train", "validation").

    Returns:
        The dataset as returned by HuggingFace datasets.
    """
    # This function is a simple wrapper; customize as needed.
    return hf_load_dataset(name, split=split)
