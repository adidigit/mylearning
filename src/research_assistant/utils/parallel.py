"""
Utilities for parallel and asynchronous execution.
"""

from __future__ import annotations

from multiprocessing import Pool
from typing import Callable, Iterable, List, Any


def run_in_parallel(func: Callable[[Any], Any], tasks: Iterable[Any], num_workers: int = 4) -> List[Any]:
    """
    Run a function over an iterable of tasks using a process pool.

    Args:
        func: Function to execute.
        tasks: Iterable of input items.
        num_workers: Number of worker processes.

    Returns:
        List of results.
    """
    with Pool(processes=num_workers) as pool:
        results = pool.map(func, tasks)
    return results
