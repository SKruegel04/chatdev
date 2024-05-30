# Requirements

- Docker
- VSCode

# Cloning and opening

1. Clone the repository
2. Open repository in VSCode
3. Click "Open in container" in the notification at the bottom right
4. Copy `.env` file into a `.env.local` file and configure the API Keys in it

If the notification doesn't appear, use `F1` and enter `reopen` to find the
`Rebuild and reopen in container` command.

# Installation

Once VSCode opened in the container, run

```bash
pip install -r requirements.txt
```

# Usage

```bash
python -m chatdev
```

