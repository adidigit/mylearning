# AI Research Assistant

The **AI Research Assistant** is an internal research and retrieval‑augmented generation (RAG) experimentation platform.  
It helps machine‑learning and research teams load datasets, build document indexes, run RAG queries and LLM inference, and manage experiments in a reproducible manner.  

## Features

* **Dataset and document handling** – load structured or unstructured datasets from local folders or HuggingFace, explore statistics with pandas, and validate schema using Pydantic models.
* **RAG experimentation** – build indexes via LlamaIndex, construct retrieval pipelines via LangChain, and compare different strategies.
* **Inference layer** – run LLM inference using vLLM for efficient serving, with optional multi‑GPU support via Accelerate.
* **Experiment management** – use Hydra to manage experiment configurations, track inputs/outputs, and reproduce results.
* **CLI‑first interface** – expose all functionality through a command line interface built with Typer.

## Getting started

This repository currently contains a skeleton structure to help teams build the AI Research Assistant.  
The project uses modern tooling—`poetry` for packaging, `pytest` for testing, GitHub Actions for CI, and `typing` for static type hints.

### Requirements

* Python 3.10+
* Poetry or uv for dependency management
* Optional: CUDA‑enabled GPU for vLLM inference

### Installation

Clone the repository and install dependencies using `poetry`:

```bash
git clone <your‑repo‑url>
cd ai‑research‑assistant
poetry install
```

You can also use `uv` if you prefer a faster dependency resolver:

```bash
uv venv
uv pip install -r requirements.txt
```

### Usage

Commands are exposed through the CLI defined in `src/research_assistant/cli/main.py`.  
Below are a few examples (to be implemented):

```bash
# Load a dataset from HuggingFace
research-assistant dataset load --name squad --split train

# Build an index from a folder of documents
research-assistant index build --path data/docs/

# Run a RAG query
research-assistant query "What is ColBERT?"
```

## Repository structure

```
ai-research-assistant/
├── src/
│   └── research_assistant/
│       ├── __init__.py
│       ├── cli/
│       │   └── main.py
│       ├── data/
│       │   └── loader.py
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── langchain_pipeline.py
│       │   └── llamaindex_pipeline.py
│       ├── inference/
│       │   ├── __init__.py
│       │   ├── vllm_engine.py
│       │   └── accelerate_runner.py
│       ├── experiments/
│       │   └── runner.py
│       ├── configs/
│       │   └── config_schema.py
│       └── utils/
│           ├── __init__.py
│           ├── parallel.py
│           ├── errors.py
│           └── typing.py
├── configs/
│   └── exp1.toml
├── tests/
│   └── test_dummy.py
├── pyproject.toml
└── .github/
    └── workflows/
        └── ci.yml
```

## Next steps

This skeleton provides the foundation for building a fully‑functional AI Research Assistant.  
You can start by fleshing out the modules under `src/research_assistant` and writing corresponding tests under `tests/`.

For more details about the intended functionality and architecture, see the accompanying specification document (to be added).
