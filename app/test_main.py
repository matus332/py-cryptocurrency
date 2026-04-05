from app.main import cryptocurrency_action
from unittest.mock import patch
from typing import Union

@patch("app.main.get_exchange_rate_prediction")
def test_to_buy_more_crypto(mocked_rate: Union[int, float]) -> None:
    mocked_rate.return_value = 4

    assert cryptocurrency_action(2) == "Buy more cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_to_sell_crypto(mocked_rate: Union[int, float]) -> None:
    mocked_rate.return_value = 1

    assert cryptocurrency_action(2) == "Sell all your cryptocurrency"


@patch("app.main.get_exchange_rate_prediction")
def test_to_do_nothing_with_105_procent(mocked_rate: Union[int, float]) -> None:
    mocked_rate.return_value = 1.05

    assert cryptocurrency_action(1) == "Do nothing"

@patch("app.main.get_exchange_rate_prediction")
def test_to_do_nothing_with_95_procent(mocked_rate: Union[int, float]) -> None:
    mocked_rate.return_value = 0.95

    assert cryptocurrency_action(1) == "Do nothing"