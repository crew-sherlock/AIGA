# Contributing PromptFlow

## Structure of a flow

- **flow.dag.yaml**: The flow definition with inputs/outputs, nodes, tools and variants for authoring purpose.
- **.promptflow/flow.tools.json**: It contains tools meta referenced in flow.dag.yaml.
- **Source code files (.py, .jinja2)**: User managed, the code scripts referenced by tools.
- **requirements.txt**: Python package dependencies for this flow.

## Generating `requirements.txt`

AIGA leverages [poetry](https://python-poetry.org/) for managing Python dependencies. However, at present PromptFlow requires `requirements.txt` for installing dependencies in the flow's runtime environment.

To manage this, we maintain two Poetry [dependency groups](https://python-poetry.org/docs/managing-dependencies/#dependency-groups) in the project's `pyproject.toml`. Using a `pre-commit` hook, we export these groups to the appropriate `requirements.txt` file.

- `promptflow-run` is exported to "promptflow/*/standard/requirements.txt"
- `promptflow-eval` is exported to "promptflow/*/evaluation/requirements.txt"

### Maintaining dependencies

1. Adding a new dependency to `promptflow-run`:

    ```bash
    poetry add <package-name> --group promptflow-run
    ```

1. Removing a dependency from `promptflow-run`:

    ```bash
    poetry remove <package-name> --group promptflow-run
    ```

1. Export dependencies to `requirements.txt`:

    ```bash
    make requirements
    ```

    > If you have recently added, removed, or updated dependencies in the `pyproject.toml`, it is likely Poetry will fail to export the dependencies. You will receive an error similar to:
    >
    > **"pyproject.toml changed significantly since poetry.lock was last generated."**
    >
    > To resolve this, you can run `poetry lock --no-update` to update the `poetry.lock` file.