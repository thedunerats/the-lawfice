import pytest

from src.src.services import email_service
from src.src.services.email_service import is_valid_email
from unittest.mock import patch, Mock


@pytest.fixture(autouse=True)
def mock_sendgrid_send_email():
    mock_sendgrid_send = Mock(name='mock_sendgrid_send')
    mock_sendgrid_send.send.side_effect = {

    }


@pytest.mark.parametrize('email, result', ([
    ('some-email-address', False),
    ('', False),
    ('999', False),
    ('email.example.com', False),
    ('email@example@example.com', False),
    ('.email@example.com', False),
    ('email.@example.com', False),
    ('email..email@example.com', False),
    ('scott@bassinlaw.net', True),
]))
def test_input_email_returns_as_expected(email, result):
    assert is_valid_email(email) == result

# need to mock sendgrid for a test here, so we will do that.
