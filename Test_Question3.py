import pytest
from unittest.mock import patch

def test_factorial_computation(capfd):
  import Question3
    # Define the test inputs and expected outputs
    test_inputs = [
        (4, "The factorial is: 24\n"),     # Valid input case
        (0, "The factorial is: 1\n"),      # Edge case with zero
        (5, "The factorial is: 120\n"),    # Another valid input case
    ]
    
    for test_input, expected_output in test_inputs:
        with patch('builtins.input', return_value=test_input):
            with patch('builtins.print') as mocked_print:
                # The logic from the provided code
                num = int(input("Enter a non-negative integer: "))

                # Initialize the factorial variable
                factorial = 1
                
                # Prompt the user for a non-negative integer until valid input is given
                while num < 0:
                    num = int(input("Enter a non-negative integer: "))
                    if num < 0:
                        print("A non-negative number is required. Please try again.")
                
                # If the user enters 0, the factorial is 1 (by definition)
                if num == 0:
                    factorial = 1
                else:
                    # Use a while loop to compute the factorial
                    while num > 1:
                        factorial *= num
                        num -= 1
                
                # Print the computed factorial
                print(f"The factorial is: {factorial}")

        # Capture the printed output
        out, _ = capfd.readouterr()
        
        # Assert that the output matches the expected result
        assert out == expected_output
