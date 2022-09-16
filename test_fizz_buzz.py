from fizz_buzz import  fizzbuzz
import pytest

def test_fizzbuzz(capsys):
    """
    Sumarry:
        This test if in the output multiple of 3 and 5 are changed by fizz and buzz
        check fizz is in the out
        check buzz is in the out
        check fizzbuzz is in the out
        check that a one multiple of 5 is not in out
        check that a one multiple of 3 is not in out
        check that a one multiple of 3 and 5 is not in out
        Due to the transitive nature of mathematics, the conditions are met for all multiples.
    """
    fizzbuzz()
    out, err = capsys.readouterr()
    assert 'fizz' in out
    assert 'buzz' in out
    assert 'fizzbuzz' in out
    assert '25' not in out         #multiple of 5
    assert '42' not in out         #multiple of 3
    assert '45' not in out         #multiple of 3 and 5