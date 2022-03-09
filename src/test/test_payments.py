import pytest
from payments import Payments

@pytest.mark.parametrize(
    "input, expected",
    [
       ((0,1,20), 20),
       ((10,12,25), 50),
       ((23,24,20), 20),
       ((10,20,20), 200),
       ((23,0,10), 10),
       ((23,24,15), 15),
       
    ]
)
def test_calculate_payment(input,expected):
    payment=Payments()
    #time in seconds

    start_time=input[0]*3600 
    end_time=input[1]*3600
    hour_cost=input[2]
    calculated_payment=payment.calculate_payment(start_time, end_time, hour_cost)
    assert calculated_payment==expected


@pytest.mark.parametrize(
    "input, expected",
    [
       ((5,8,'MO'), 75),
       ((10,12,'WE'), 30),
       ((20,22,'SA'), 50),
       
    ]
)
def test_calculate_total_payment(input,expected):
    payment=Payments()
    #time in seconds

    start_time=input[0]*3600 
    end_time=input[1]*3600
    day=input[2]
    calculated_total_payment=payment.calculate_total_payment(day, start_time, end_time)
    assert calculated_total_payment==expected