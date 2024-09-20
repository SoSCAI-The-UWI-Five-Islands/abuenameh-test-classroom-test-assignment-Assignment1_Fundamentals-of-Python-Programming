import math
from unittest.mock import patch
import pytest

def test_garden_requirements(capfd):
    import Question1
    # Patch input to simulate user input
    inputs = iter([16, 2, 1, 0.5])
    
    with patch('builtins.input', lambda _: next(inputs)):
        # Run the original code block to simulate the garden calculations
        cubic_feet_per_cubic_yard = 27
        print("Calculate Garden requirements")
        print("-----------------------------")
        side = float(input("Enter length of side of garden (feet): "))
        spacing = float(input("Enter spacing between plants (feet): "))
        d1 = float(input("Enter depth of garden soil (feet): "))
        d2 = float(input("Enter depth of fill (feet): "))
        print()

        r = side / 4
        circle_bed_area = math.pi * r ** 2
        semicircle_bed_area = circle_bed_area / 2
        total_bed_area = 3 * math.pi * r ** 2
        fill_area = side ** 2 - total_bed_area

        plant_area = spacing ** 2
        plants_for_semicircle = int(semicircle_bed_area / plant_area)
        plants_for_circle = int(circle_bed_area / plant_area)

        print("-----------------------------")
        print("Requirements")
        print()
        print("Plants for each semicircle garden:", plants_for_semicircle)
        print("Plants for the circle garden:", plants_for_circle)
        print("Total plants for garden:", 4 * plants_for_semicircle + plants_for_circle)
        print("Soil for each semicircle garden:", round(semicircle_bed_area * d1 / cubic_feet_per_cubic_yard, 1), "cubic yards")
        print("Soil for the circle garden:", round(circle_bed_area * d1 / cubic_feet_per_cubic_yard, 1), "cubic yards")
        print("Total soil for the garden:", round(total_bed_area * d1 / cubic_feet_per_cubic_yard, 1), "cubic yards")
        print("Total fill for the garden:", round(fill_area * d2 / cubic_feet_per_cubic_yard, 1), "cubic yards")

    # Capture printed output
    out, _ = capfd.readouterr()

    # Split the output lines and strip any extra spaces
    output_lines = [line.strip() for line in out.split('\n') if line.strip()]

    # Assertions on printed values
    assert "Plants for each semicircle garden: 25" in output_lines
    assert "Plants for the circle garden: 50" in output_lines
    assert "Total plants for garden: 150" in output_lines
    assert "Soil for each semicircle garden: 4.6 cubic yards" in output_lines
    assert "Soil for the circle garden: 9.3 cubic yards" in output_lines
    assert "Total soil for the garden: 27.8 cubic yards" in output_lines
    assert "Total fill for the garden: 42.8 cubic yards" in output_lines

def test_small_garden_requirements(capfd):
    import Question1
    # Patch input to simulate user input
    inputs = iter([8, 1.5, 0.5, 0.25])

    with patch('builtins.input', lambda _: next(inputs)):
        # Run the original code block to simulate the garden calculations
        cubic_feet_per_cubic_yard = 27
        print("Calculate Garden requirements")
        print("-----------------------------")
        side = float(input("Enter length of side of garden (feet): "))
        spacing = float(input("Enter spacing between plants (feet): "))
        d1 = float(input("Enter depth of garden soil (feet): "))
        d2 = float(input("Enter depth of fill (feet): "))
        print()

        r = side / 4
        circle_bed_area = math.pi * r ** 2
        semicircle_bed_area = circle_bed_area / 2
        total_bed_area = 3 * math.pi * r ** 2
        fill_area = side ** 2 - total_bed_area

        plant_area = spacing ** 2
        plants_for_semicircle = int(semicircle_bed_area / plant_area)
        plants_for_circle = int(circle_bed_area / plant_area)

        print("-----------------------------")
        print("Requirements")
        print()
        print("Plants for each semicircle garden:", plants_for_semicircle)
        print("Plants for the circle garden:", plants_for_circle)
        print("Total plants for garden:", 4 * plants_for_semicircle + plants_for_circle)
        print("Soil for each semicircle garden:", round(semicircle_bed_area * d1 / cubic_feet_per_cubic_yard, 1), "cubic yards")
        print("Soil for the circle garden:", round(circle_bed_area * d1 / cubic_feet_per_cubic_yard, 1), "cubic yards")
        print("Total soil for the garden:", round(total_bed_area * d1 / cubic_feet_per_cubic_yard, 1), "cubic yards")
        print("Total fill for the garden:", round(fill_area * d2 / cubic_feet_per_cubic_yard, 1), "cubic yards")

    # Capture printed output
    out, _ = capfd.readouterr()

    # Split the output lines and strip any extra spaces
    output_lines = [line.strip() for line in out.split('\n') if line.strip()]

    # Assertions on printed values
    assert "Plants for each semicircle garden: 4" in output_lines
    assert "Plants for the circle garden: 8" in output_lines
    assert "Total plants for garden: 24" in output_lines
    assert "Soil for each semicircle garden: 0.9 cubic yards" in output_lines
    assert "Soil for the circle garden: 1.9 cubic yards" in output_lines
    assert "Total soil for the garden: 5.6 cubic yards" in output_lines
    assert "Total fill for the garden: 8.6 cubic yards" in output_lines
