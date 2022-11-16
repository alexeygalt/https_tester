import pytest
from utils import get_valid_email

get_valid_email_param = ['https://google.com', 'https://www.facebook.com', 'http://fapl.com',
                         'https://ru.wikipedia.org']
get_not_valid_email_param = ["hello", "https:/google.com", "htps://www.facebook.com"]
get_valid_email_exceptions = [(2022, TypeError), (3.22, TypeError)]


@pytest.mark.parametrize('stdin', get_valid_email_param)
def test_get_valid_email_param(stdin):
    assert get_valid_email(stdin)


@pytest.mark.parametrize('stdin', get_not_valid_email_param)
def test_get_not_valid_email_param(stdin):
    assert not get_valid_email(stdin)


# test module validators to int | float arguments
@pytest.mark.parametrize('stdin, exceptions', get_valid_email_exceptions)
def test_get_valid_email_exceptions(stdin, exceptions):
    with pytest.raises(exceptions):
        get_valid_email(stdin)
