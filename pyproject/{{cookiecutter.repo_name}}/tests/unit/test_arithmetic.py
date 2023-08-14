from {{ cookiecutter.package_name }}.arithmetic import add


def test_add() -> None:
    assert add(1, 2) == 3
