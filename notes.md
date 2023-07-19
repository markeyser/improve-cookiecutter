# Ruff Notes

- Use a single linter: Ruff
- Ruff can replace PyLint and Flake8 and many more


```bash
$ ruff src/*.py
error: Failed to parse src/example.py:8:1: Unexpected token Indent
src/example.py:3:89: E501 Line too long (90 > 88 characters)
src/example.py:8:1: E999 SyntaxError: Unexpected token Indent
src/example_2.py:4:5: F841 [*] Local variable `name` is assigned to but never used
src/example_2.py:7:23: F821 Undefined name `nam`
src/example_2.py:14:89: E501 Line too long (169 > 88 characters)
Found 5 errors.
```

## Configuring Ruff on VS Code

### Install Ruff Python package on your virtual environment

Ruff is included as part of the `requirements.txt`. So, Ruff must be par
of your Python virtual environment.

### Using Ruff VS code extension

Ruff VS Code extension is already part of the `.vscode/extensions.json`
file. So, Ruff's VS Code extension must be already part of your
workspace-level extensions.

To configure Ruff VS Code extension include the following on the
`.vscode/settings.json`:

To autofix violations on-save using Ruff, then re-format with Black, via
the following `settings.json`:

```json
{
  "[python]": {
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
      "source.fixAll": true
    }
  },
  "python.formatting.provider": "black"
}
```

Also include the following:

```json
    // ##################################
    // ### Ruff linter configuration  ###
    // ##################################
    // Path to the pyproject.toml
    "ruff.args": [
        "--config=pyproject.toml"
    ],
    // Path to a custom ruff executable
    "ruff.path": [
        "./venv/bin/ruff"
    ],
    // Path to the Python interpreter use to run the linter sever
    "ruff.interpreter": [
        "./venv/bin/python"
    ],
```

### Configuration

Ruff can be configured through a `pyproject.toml`, `ruff.toml`, or
`.ruff.toml` file.

Notice that probably it is not a good idea to use a linter in Notebooks.
Notebooks are for exploration. So, maybe only on the py scripts. But
maybe all developers are going to start using only the notebooks so...
yes, maybe it is a better idea to force to pass the linter to all code.

```toml
[tool.ruff]
select = ["ALL"]
# To ignore all rules with a common pre-fix use *
ignore = ["ANN*"]
# Decrease the maximum line length to 79 characters.
line-length = 79
# To opt in to linting Jupyter Notebook
# The include parameter is for Jupyter Notebooks and not
# for Jupyter Notebook in VS Code. Jupyter Notebook in 
# VSCode isn't supported yet:
# https://github.com/astral-sh/ruff-vscode/issues/256
# See also discussion on Discord
include = ["*.py", "*.pyi", "**/pyproject.toml", "*.ipynb"]
```