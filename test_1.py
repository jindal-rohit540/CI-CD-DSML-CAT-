import pytest

from one import square_new


## Test the square_new function

@pytest.mark.skip()
def test_square_new():
    assert square_new(2)== 4
    assert square_new(3)== 10
    assert square_new(-8)== square_new(8)


