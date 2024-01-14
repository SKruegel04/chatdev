# Requirements

- Docker
- VSCode

# Cloning and opening

1. Clone the repository
2. Open repository in VSCode
3. Click "Open in container" in the notification at the bottom right
4. Copy `.env` file into a `.env.local` file and configure the OAI API Key in it

If the notification doesn't appear, use `F1` and enter `reopen` to find the
`Rebuild and reopen in container` command.

# Installation

Once VSCode opened in the container, run

```bash
pip install -r requirements.txt
```

# Structure

```
/.devcontainer      VSCode Devcontainer Configuration
/.vscode            VSCode Configuration
/notebooks          Jupyter Notebooks for experiments and implementations
  /chat-dev.ipynb   The final Notebook for presentation
/.env               An example for environment variable configuration
/.env.local         Needs to be created by the developer
/.gitignore         Ignore file for Git
/README.md          This README file
/requirements.txt   Python dependencies
```
