import pytest
from unittest.mock import patch
import io

# Corrected code placed in a function for testing
def student_grades():
    num_students_input = input("Enter the number of students: ")
    num_students = int(num_students_input)
    if num_students <= 0:
        print("Please enter a positive number.")
    else:
        for i in range(num_students):
            print(f"\nEnter data for student {i + 1}:")
            
            name = input("Name: ")
            score1_input = input("Score on test #1: ")
            score2_input = input("Score on test #2: ")
            score1 = float(score1_input)
            score2 = float(score2_input)
            
            average = (score1 + score2) / 2
            
            if 80 < average <= 100:
                letter_grade = 'A'
            elif 60 < average <= 80:
                letter_grade = 'B'
            elif 49 < average <= 60:
                letter_grade = 'C'
            else:
                letter_grade = 'F'
            
            print(f"{name}: {letter_grade}")

@patch('builtins.input', side_effect=['2', 'Alice', '85', '90', 'Bob', '55', '60'])
@patch('sys.stdout', new_callable=io.StringIO)
def test_student_grades(mock_stdout, mock_input):
    student_grades()
    
    # Check the output
    output = mock_stdout.getvalue()
    
    assert "Enter data for student 1:" in output
    assert "Alice: A" in output
    assert "Enter data for student 2:" in output
    assert "Bob: B" in output
