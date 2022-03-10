import pytest
from shift import Shift

@pytest.mark.parametrize(
    "input, expected",
    [
       ((10, 11), ('noon', 'noon')),
       ((5, 8), ('morning', 'morning')),
       ((5, 10), ('morning', 'noon')),
       ((5, 20), ('morning', 'night'))
    ]
)
def test_parse_employee_name(input,expected):
    start_hour_string=input[0]*3600
    end_hour_string=input[1]*3600
    shift=Shift(start_hour_string, end_hour_string)
    assert (shift.time_in.schedule, shift.time_out.schedule)==expected
