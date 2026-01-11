######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################

import os.path
import sys
import unittest

test_file = "lab2_problem3"
test_inputs = ['hello', 'goodbye']

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

    # Test: Ensure 3 lines of output
    assert len(output) == 3
    
    # Test: Ensure charset matches selection
    assert output[0] == 'hellogoodbye'
    assert output[1] == 'hellohellohellohellohello'
    assert int(output[2]) == 12

######################################
## WARNING! DO NOT MODIFY THIS FILE ##
######################################