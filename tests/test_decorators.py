import pytest

from src.decorators import log


def test_log_error_console(capsys) -> None:

    @log()
    def foo(x:int, y:int) -> None:
        return x + y

    with pytest.raises(TypeError):
        foo(2, "3")
        captured = capsys.readouterr()
        assert "foo - <class 'TypeError'> - args: (2, '3') - kwargs: {}\n\n" == captured


def test_log_success_file() -> None:

    file_name = "tests/test.txt"

    @log(filename=file_name)
    def foo(x, y) -> None:
        return x + y

    result = foo(2, 3)
    assert result == 5

    with open(file_name, "r", encoding="utf-8") as f:
        content = f.readlines()
        assert content[-1] == "foo - OK - 5\n"
