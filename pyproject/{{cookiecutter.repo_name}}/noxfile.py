import nox


PATHS_TO_CHECK_STYLE = ["src", "tests"]


@nox.session
def auto_format(session):
    session.run("isort", *PATHS_TO_CHECK_STYLE, external=True)
    session.run("black", *PATHS_TO_CHECK_STYLE, external=True)


@nox.session
def check_format(session):
    session.run("isort", "--check", *PATHS_TO_CHECK_STYLE, external=True)
    session.run("black", "--check", *PATHS_TO_CHECK_STYLE, external=True)


@nox.session
def run_flake8(session):
    session.run("flake8", *PATHS_TO_CHECK_STYLE, external=True)


@nox.session
def run_mypy(session):
    session.run("mypy", external=True)


@nox.session
def run_unit_tests(session):
    session.run("pytest", "tests/unit", external=True)


# Exclude auto_format from default sessions
nox.options.sessions = [
    f.__name__ for f in [check_format, run_flake8, run_mypy, run_unit_tests]
]
