"""
Configuration schema for research_assistant.

Defines dataclasses representing sections of experiment configuration: DatasetConfig,
RetrievalConfig, InferenceConfig, ParallelConfig, and ExperimentConfig aggregator.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class DatasetConfig:
    """Configuration for dataset loading."""

    source: str
    name: str
    split: str = "train"


@dataclass
class RetrievalConfig:
    """Configuration for retrieval pipeline."""

    engine: str
    embedding_model: Optional[str] = None
    index_path: Optional[str] = None


@dataclass
class InferenceConfig:
    """Configuration for inference engine."""

    model: str
    batch_size: int = 1
    device: str = "cuda"


@dataclass
class ParallelConfig:
    """Configuration for parallel execution."""

    num_workers: int = 1
    use_gpu: bool = False


@dataclass
class ExperimentConfig:
    """Aggregated configuration for an experiment."""

    dataset: DatasetConfig
    retrieval: RetrievalConfig
    inference: InferenceConfig
    parallel: ParallelConfig
