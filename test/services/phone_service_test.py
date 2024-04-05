import pytest

from src.src.services.phone_service import is_phone_number


@pytest.mark.parametrize('number, result', ([
    ('some-phone-number', False),
    ('', False),
    ('999', False),
    ('444444', False),
    ('666 666', False),
    ('14157535245', True),
    ('4157535245', True),
    ('(123) 456-7890', True),
    ('123-456-7890', True),
    ('123.456.7890', True),
    ('+91 (123) 456-7890', True),
]))
def test_input_phone_number_returns_as_expected(number, result):
    assert is_phone_number(number) == result
