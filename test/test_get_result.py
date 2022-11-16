from utils import get_result, get_simple_gen
import pytest

get_result_param = [get_simple_gen('https://google.com', 'https://ru.wikipedia.org')]


@pytest.mark.parametrize('stdin', get_result_param)
def test_get_result_param_v1(stdin):
    assert get_result(*stdin)['https://google.com'] == {'GET': 200, 'HEAD': 301}


get_result_param = [get_simple_gen('https://google.com')]


@pytest.mark.parametrize('stdin', get_result_param)
def test_get_result_param_v2(stdin):
    assert type(get_result(*stdin)) == dict


get_result_param = [get_simple_gen('https://google.com')]


@pytest.mark.parametrize('stdin', get_result_param)
def test_get_result_param_v3(stdin):
    assert len(get_result(*stdin)) == 1


get_result_param = [get_simple_gen('https://ru.wikipedia.org')]


@pytest.mark.parametrize('stdin', get_result_param)
def test_get_result_param_v4(stdin):
    assert get_result(*stdin)['https://ru.wikipedia.org'] == {'GET': 200, 'PUT': 200, 'DELETE': 200, 'HEAD': 301,
                                                              'PATCH': 200}

