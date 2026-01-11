######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab2_problem2"
test_inputs = [5, 41]

def test(monkeypatch, capsys):
    global test_file
    global test_inputs
    try:
        exists = os.path.exists(test_file + '.py')
        assert exists == True
        source = __import__(test_file)
    except:
        sys.exit()
    if len(test_inputs) > 0:
        inputs = iter(test_inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    source.main()
    captured = capsys.readouterr()
    output = captured.out.split('\n')
    output.pop() # Remove last blank line since split by \n

    tc = unittest.TestCase()

    # Test: Ensure 6 lines of output
    assert len(output) == 6
    
    # Test: Ensure charset matches selection
    assert int(output[0]) == 46
    assert int(output[1]) == -36
    assert int(output[2]) == 205
    assert round(float(output[3]), 1) == 0.1
    assert int(output[4]) == 1706
    assert int(output[5]) ==  5

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################