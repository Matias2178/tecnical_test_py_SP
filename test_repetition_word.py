from repetition_word import repetition_word
import pytest

tex_for_test = "Hi!| ° ¬ how, are. \n  hI things? How are you? Are you a developer? I am also a developer"

def test_repetition_word(capsys):
    """"    
    Sumarry:
        Given a text, of which we know the number of repetitions, 
        special characters are added to control the correct operation.
    """
    repetition_word(tex_for_test)
    out, err = capsys.readouterr()
    assert 'hi 2' in out
    assert 'how 2' in out
    assert 'are 3' in out
    assert 'things 1' in out
    assert 'you 2' in out
    assert 'a 2' in out
    assert 'developer 2' in out
    assert 'i 1' in out
    assert 'am 1' in out
    assert 'also 1' in out 

    