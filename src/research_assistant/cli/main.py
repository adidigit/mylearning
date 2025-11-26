"""
Entry point for the AI Research Assistant command‑line interface.

This module uses Typer to expose subcommands for dataset loading,
index construction, querying and experiment execution. Each command is
currently a stub and should be implemented by the development team.
"""

import typer

app = typer.Typer(help="AI Research Assistant CLI")


@app.command()
def dataset_load(name: str = typer.Argument(..., help="Name of the dataset"), split: str = "train") -> None:
    """Load a dataset by name.

    This command should load the specified dataset into an internal
    format using the datasets library.

    Args:
        name: Dataset identifier (e.g., 'squad').
        split: Split name (e.g., 'train', 'test').
    """
    # TODO: Implement dataset loading using `datasets` library
    typer.echo(f"Loading dataset '{name}' (split: {split})…")


@app.command()
def index_build(path: str = typer.Argument(..., help="Path to documents")) -> None:
    """Build a document index from the specified path.

    Args:
        path: Path to a folder containing source documents.
    """
    # TODO: Implement indexing via LlamaIndex
    typer.echo(f"Building index from documents in '{path}'…")


@app.command()
def query(question: str = typer.Argument(..., help="Question to ask")) -> None:
    """Run a RAG query against the indexed documents.

    Args:
        question: Natural language query.
    """
    # TODO: Implement retrieval and LLM inference via LangChain / LlamaIndex / vLLM
    typer.echo(f"Running query: {question}")


@app.command()
def run(config: str = typer.Option("configs/exp1.toml", help="Path to the experiment config file")) -> None:
    """Run an experiment defined by a configuration file.

    Args:
        config: Path to a `.toml` or `.yaml` config file for Hydra.
    """
    # TODO: Implement experiment runner using Hydra
    typer.echo(f"Running experiment using config '{config}'…")


def main() -> None:
    """Entry point for standalone execution."""
    app()


if __name__ == "__main__":
    main()
