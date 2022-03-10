import pytest
from main import process_payment

@pytest.mark.parametrize(
    "input, expected",
    [
       ('RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'The amount to pay RENE is: 215 USD'),
       ('ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00', 'The amount to pay ASTRID is: 85 USD'),
       ('MANUEL=MO04:00-19:00', 'The amount to pay MANUEL is: 280 USD'),
       ('JUAN=MO08:00-12:00,TH15:00-13:00', 'Error in data for employee JUAN')
    ]
)
def test_process_payment(input,expected):
    output=process_payment(input)
    assert output==expected