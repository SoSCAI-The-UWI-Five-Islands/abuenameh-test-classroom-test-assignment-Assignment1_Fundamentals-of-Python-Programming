import pytest
import math
from unittest.mock import patch

def test_square_root_calculations(capfd):
  import Question2
    test_input = "20"
    
    with patch('builtins.input', return_value=test_input):
        num = float(input("Enter a number greater than 2: "))
        
        assert num > 2, "Input number is not greater than 2"  
        
        count = 0
        
        while num >= 2:
            num = math.sqrt(num)
            count += 1
            print(f"{count}: {num:.3f}")
        
    out, _ = capfd.readouterr()
  
    expected_output = "1: 4.472\n2: 2.115\n3: 1.454\n"
    assert out == expected_output


