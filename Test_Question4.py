import pytest
from unittest.mock import patch

def test_point_in_rectangle(capfd):
  import Question4
    # Define test cases with inputs and expected outputs
    test_cases = [
        # Inside the rectangle
        ( "(1, 1)", "Point (1, 1) is in the rectangle\n" ),
        ( "(4, 1)", "Point (4, 1) is in the rectangle\n" ),
        ( "(0, 2.5)", "Point (0, 2.5) is in the rectangle\n" ),
        
        # Outside the rectangle
        ( "(6, 1)", "Point (6, 1) is not in the rectangle\n" ),
        ( "(1, 3)", "Point (1, 3) is not in the rectangle\n" ),
        ( "(6, 3)", "Point (6, 3) is not in the rectangle\n" ),
    ]

    for point_input, expected_output in test_cases:
        with patch('builtins.input', return_value=point_input):
            with patch('builtins.print') as mocked_print:
                # The logic from the provided code
                x, y = eval(input("Enter a point with two coordinates: "))

                # Compute the horizontal distance to the center of the rectangle
                hDistance = (x * x) ** 0.5

                # Compute the vertical distance to the center of the rectangle
                vDistance = (y * y) ** 0.5

                if (hDistance <= 5 and vDistance <= 2.5):
                    print("Point (" + str(x) + ", " + str(y) + ") is in the rectangle")
                else:
                    print("Point (" + str(x) + ", " + str(y) + ") is not in the rectangle")

        # Capture the printed output
        out, _ = capfd.readouterr()

        # Assert that the output matches the expected result
        assert out == expected_output
