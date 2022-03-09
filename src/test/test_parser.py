import pytest
from parser import Parser

@pytest.mark.parametrize(
    "input, expected",
    [
       ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'RENE'),
       ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'ASTRID'),
    ]
)
def test_parse_employee_name(input,expected):
    parser=Parser(input)
    employee=parser.get_employee()
    assert employee==expected

@pytest.mark.parametrize(
    "input, expected",
    [
       ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', ['MO', 'TU', 'TH', 'SA', 'SU']),
       ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', ['MO', 'TH', 'SU'] ),
    ]
)
def test_parse_work_days(input, expected):
    parser=Parser(input)
    workdays=parser.get_workdays()
    assert workdays==expected


@pytest.mark.parametrize(
    "input, expected",
    [
       ('MO10:00-12:00', (True, 'MO', 36000, 43200)),
       ('TH01:00-03:00', (True, 'TH', 3600*1, 3600*3)),
       ('TH03:00-01:00', (False, 'TH', 3600*3, 3600*1)),
       ('FY10:00-11:00', (False, 'FY', 3600*10, 3600*11)),
    ]
)
def test_parse_shift(input, expected):
    parser=Parser()
    shift=parser.get_work_shift(input)
    assert shift==expected
