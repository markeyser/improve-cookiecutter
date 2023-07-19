# Working On Cookiecutter

Improving Cookiecutter template

## Directory Structure

```text
├── .env                        <- Environment variables for the project.
├── .github                     <- GitHub-specific settings and configurations.
│   ├── CODEOWNERS              <- Specifies individuals or teams that are responsible for code in a repository.
│   ├── ISSUE_TEMPLATE          <- Templates for issues to be used by contributors.
│   │   ├── ask_issues_template.md         <- Issue template for asking questions.
│   │   ├── bug_report_template.md         <- Issue template for reporting bugs.
│   │   ├── data_aquisition_template.md    <- Issue template for data acquisition tasks.
│   │   ├── data_creation_template.md      <- Issue template for data creation tasks.
│   │   ├── experiment_issues_template.md  <- Issue template for experiment tasks.
│   │   ├── explore_issues_template.md     <- Issue template for exploration tasks.
│   │   ├── feature_request.md             <- Issue template for feature requests.
│   │   └── model_issues_templates.md      <- Issue template for model-related tasks.
│   └── PULL_REQUEST_TEMPLATE   <- Templates for pull requests to be used by contributors.
│       └── pull_request_template.md
├── .gitignore                  <- Specifies intentionally untracked files to ignore.
├── .pre-commit-config.yaml     <- Configuration for pre-commit hooks to enforce coding style and checks.
├── .vscode                     <- Configuration for Visual Studio Code editor.
│   ├── extensions.json         <- Specifies extensions recommended for the project in VS Code.
│   └── settings.json           <- Project-specific settings for VS Code.
├── Makefile                    <- Makefile with commands like `make data` or `make train`.
├── READMEmd                    <- The top-level README for developers using this project.
├── configuration               <- Directory for project configuration files.
├── data                        <- Data for the project, divided into different stages of data processing.
│   ├── external                <- Data from third party sources.
│   ├── interim                 <- Intermediate data that has been transformed.
│   ├── processed               <- The final, canonical data sets for modeling.
│   └── raw                     <- The original, immutable data dump.
├── docs                        <- Directory for project documentation.
├── mkdocs.yml                  <- Configuration file for the MkDocs documentation tool.
├── notebooks                   <- Jupyter notebooks for data exploration and experimentation.
├── pyproject.toml              <- Specifies dependencies for the project in a format that pip can understand.
├── requirements.txt            <- The requirements file for reproducing the analysis environment.
├── setup.py                    <- Makes this project pip installable with `pip install -e`.
├── src                         <- Source code for the project.
│   └── __init__.py             <- Makes src a Python module.
└── test                        <- Directory for test files.
```

## Instructions

Before you begin, ensure you have installed Python 3.

To start working on the project, follow these steps:

1. Clone the repository:

```bash 
$ git clone https://github.com/your_username/your_repository.git $ cd
your_repository
```

2. Create a Python virtual environment with `venv` named `venv`:

```bash
$ make env_create
```

3. Depending on your operating system, activate the virtual environment using
one of the following commands:

On macOS:

```bash 
$ source venv/bin/activate
```

On Windows:

```bash
$ .\venv\Scripts\activate
```

4. Install dependencies from a requirements.txt:

```bash
$ make env_install
```

5. Make the `src` folder a Python package:

```bash
$ make src_package
```

6. You are now ready to start working on the project. When you're done, you can
deactivate the virtual environment using the following command:

```bash
$ deactivate
```

Remember, every time you want to work on the project, ensure you activate the
virtual environment, and deactivate it when you're done.

This guide assumes that you are using make commands which have been properly
defined in a Makefile for creating and managing the Python virtual environment,
installing dependencies, and making the `src` directory a Python package.

If you aren't using a Makefile, replace the make commands with the corresponding
Python commands provided in previous responses.

> When you run the `make` command in the terminal, a menu is displayed that
lists all the available options, from cleaning unused imports to creating a
Python package, each associated with a specific command for easy management of
your project workflow.