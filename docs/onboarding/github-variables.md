# GitHub Variables

AIGA uses GitHub Variables to store project-specific configuration settings. These variables are primarily used in GitHub Action workflows to control the behaviour of LLMOps.

> **Note:** By default, variables render unmasked in build outputs. Do not use variables to store sensitive information like API keys, secrets, or passwords. Instead, use [GitHub Secrets](./github-secrets.md).

## Repository Variables

An AIGA Project can configure the behaviour of the repository workflows by setting the following variables:

- `DEPLOYMENT_TARGET` - The Azure service to target for inference deployment - "aml", "webapp" or "both"
- `PROMPTFLOW_BASE_PATH` - The base path for the PromptFlow directory. E.g. "promptflow"
- `DEFAULT_ENVIRONMENT` - The default environment that the repository targets. **Note:** This variable is used in continuously running workflows such as PR, CI, CD and typically is set to the playground environment. It is overridden when running the pipelines manually to target a specific environment (i.e. `dev`, `test`, `prod`), by setting the `environment` variable.

## Environment Variables

Environment Variables are used within AIGA to control which resources are used based on the environment (e.g. `pr`, `dev`, `prod`).

The following Environment Variables are required as a pre-requisite for AIGA:

- `KEY_VAULT_NAME` - should point to the Azure Key Vault associated with the environment.
