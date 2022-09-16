import pytest
from fibonacci import fibonacci
"""
    Sumary:
        test for fibonacci function, test wrong input an some correct values
"""

@pytest.mark.parametrize("num, expected_result",[
    (-12, 144),             #test negative 
    (12.0, None),           #test non integer
    (0, 0),                 #test 0
    (1, 1),
    (2, 1),
    (3, 2),
    (4, 3),
    (5, 5),
    (6, 8),
    (7, 13),
    (8, 21),
    (9, 34),
    (10, 55),
    (1000, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875),
    (1001, 70330367711422815821835254877183549770181269836358732742604905087154537118196933579742249494562611733487750449241765991088186363265450223647106012053374121273867339111198139373125598767690091902245245323403501),
    ])

def test_fibonacci_param(num, expected_result):
    """_
    Sumarri:
        check for some values fibonacci series.
        non-permited values also are controlled
    """
    assert fibonacci(num) == expected_result
  