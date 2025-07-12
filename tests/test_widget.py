import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "x, y",
    [
        ("Счет57756830220412508888", "Счет XX8888"),
        ("Счет 87717779911111441480", "Счет XX1480"),
        ("голд 9735422221636720", "голд 9735 42XX XXXX 6720"),
        ("м52864998633331584240", "неверно указан номер"),
        ("Счет", "неверно указан номер"),
        ("Счет8218216540", "неверно указан номер"),
        ("Visa Maestro 55552cc16cc555554000", "неверно указан номер"),
    ],
)
def test_det_mask_account_card(x: str, y: str) -> None:
    assert mask_account_card(x) == y


def test_det_mask_account_card1(my_card: str) -> None:
    assert mask_account_card("МИР1234567891234567") == f"МИР {my_card}"


def test_det_mask_account_account(my_account: str) -> None:
    assert mask_account_card("Счет57756830220412508912") == f"Счет {my_account}"


def test_get_date(my_date: str) -> None:
    assert get_date("2024-12-31T02:26:18.671407") == my_date


def test_get_dat_not(not_date: str) -> None:
    assert get_date("2024-12-") == not_date


def test_get_dat_not1(not_date: str) -> None:
    assert get_date("") == not_date
