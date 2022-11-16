from typing import Iterator
import validators
import sys
from constants import METHODS


def get_valid_email(string: str) -> bool:
    """validating a string to http(s) form"""
    return validators.url(string)


def get_email_list() -> Iterator[str]:
    """take http(s) from stdin"""
    data = (item.strip() for item in sys.stdin)
    return data


def get_result(data: Iterator[str]) -> dict:
    """for every http(s) get response for methods from METHODS"""
    result = {}
    for item in data:
        tmp_dict = {}
        for key, value in METHODS.items():
            temp = value(item)
            if temp.status_code != 405:
                tmp_dict[key] = temp.status_code
        result[item] = tmp_dict

    return result


def get_simple_gen(*args):
    """make gen to tests"""
    yield args

