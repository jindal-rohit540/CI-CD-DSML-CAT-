##
from one import s, divide

## How to run test_1.py

def test_square():
    assert s(2)==4
    assert s(3)==9


def test_divide():
    assert divide(10,2)==5
    assert divide(10,5)==9
    # assert divide(10,0)==0