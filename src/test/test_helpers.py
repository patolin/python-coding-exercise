import pytest
from helpers import convert_time

@pytest.mark.parametrize(
    "input, expected",
    [
       ('01:00', 3600),
       ('17:00', 61200),
       
    ]
)
def test_convert_time(input,expected):
    output=convert_time(input)
    assert output==expected