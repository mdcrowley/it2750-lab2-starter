######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab2_problem1"
test_inputs = []

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
    assert int(output[0]) == 53
    assert int(output[1]) == 31
    assert int(output[2]) == 462
    assert round(float(output[3]), 1) == 3.8
    assert int(output[4]) == 1885
    assert int(output[5]) ==  9

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################