import types

from utils import get_email_list


def test_get_email_list():
    assert isinstance(get_email_list(), types.GeneratorType)


