# {{ cookiecutter.project_name }}

## Development
### Pre-requisites:
* Python3.11
* Poetry

### Install project dependencies
```shell
poetry install --no-root
```

### Linting and tests
Run all tests and checks:
```shell
poetry run nox --no-venv
```

Lint Python code:
```shell
poetry run nox --no-venv -s auto_format
```
