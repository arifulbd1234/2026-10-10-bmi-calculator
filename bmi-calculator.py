"""
Day 4 - 2026-10-10
Tool: BMI Calculator
What it does: Works out Body Mass Index (BMI) from height and weight,
says which standard category it falls in, and shows the healthy weight
range for that height.
Who it helps: Anyone checking their general health, starting a fitness
plan, or filling in a health form that asks for BMI.
"""


def calculate_bmi(weight_kg, height_cm):
    """Return BMI (kg/m^2) rounded to 1 decimal place."""
    if weight_kg <= 0:
        raise ValueError("Weight must be more than zero.")
    if height_cm <= 0:
        raise ValueError("Height must be more than zero.")
    height_m = height_cm / 100
    return round(weight_kg / (height_m * height_m), 1)


def bmi_category(bmi):
    """Return the standard WHO category for a BMI value."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25.0:
        return "Healthy weight"
    if bmi < 30.0:
        return "Overweight"
    return "Obese"


def healthy_weight_range_kg(height_cm):
    """Return the (low, high) healthy weight range in kg for a height.

    Based on BMI 18.5 to 24.9, rounded to 1 decimal place.
    """
    if height_cm <= 0:
        raise ValueError("Height must be more than zero.")
    height_m = height_cm / 100
    low = round(18.5 * height_m * height_m, 1)
    high = round(24.9 * height_m * height_m, 1)
    return low, high


def format_bmi(weight_kg, height_cm):
    """Return the BMI result as one easy-to-read line."""
    bmi = calculate_bmi(weight_kg, height_cm)
    return f"BMI {bmi} ({bmi_category(bmi)})"


if __name__ == "__main__":
    # Example 1: an adult checking their BMI before starting exercise
    print("70 kg, 170 cm:", format_bmi(70, 170))
    low, high = healthy_weight_range_kg(170)
    print("Healthy weight range for 170 cm:", f"{low} kg to {high} kg")

    # Example 2: a taller, heavier adult
    print("90 kg, 180 cm:", format_bmi(90, 180))

    # Example 3: a lighter adult who may need to gain weight
    print("48 kg, 165 cm:", format_bmi(48, 165))
    low, high = healthy_weight_range_kg(165)
    print("Healthy weight range for 165 cm:", f"{low} kg to {high} kg")
