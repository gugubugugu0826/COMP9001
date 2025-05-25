def calc_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculate the Body Mass Index (BMI) given weight and height.

    BMI is defined as weight in kilograms divided by the square of height in meters.

    Parameters:
        weight_kg (float): User's weight in kilograms.
        height_cm (float): User's height in centimeters.

    Returns:
        float: The BMI value.
    """
    # Convert height from centimeters to meters
    h = height_cm / 100
    # Compute BMI using the formula: weight (kg) / (height (m) ^ 2)
    return weight_kg / (h * h)


def calc_bmr(weight_kg: float, height_cm: float, age: int, gender: str) -> float:
    """
    Calculate the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor equation.

    BMR represents the number of calories required to keep your body functioning at rest.

    Parameters:
        weight_kg (float): User's weight in kilograms.
        height_cm (float): User's height in centimeters.
        age (int): User's age in years.
        gender (str): User's gender, expected values 'man' or 'woman' (case-insensitive).

    Returns:
        float: The estimated BMR in kilocalories per day.
    """
    # Normalize gender input to lowercase for comparison
    gender_key = gender.lower()

    if gender_key == 'man' or gender_key == 'male':
        # Mifflin-St Jeor formula for males:
        #   BMR = (10 × weight_kg) + (6.25 × height_cm) − (5 × age) + 5
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5

    elif gender_key == 'woman' or gender_key == 'female':
        # Mifflin-St Jeor formula for females:
        #   BMR = (10 × weight_kg) + (6.25 × height_cm) − (5 × age) − 161
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # If gender is unrecognized, optionally raise an error or return None
    raise ValueError("Gender must be 'man' or 'woman'")


def calc_water_intake(weight_kg: float, activity_level: str) -> float:
    """
    Estimate the recommended daily water intake based on body weight and activity level.

    Base recommendation is 35 ml per kilogram of body weight, adjusted by activity factor.

    Parameters:
        weight_kg (float): User's weight in kilograms.
        activity_level (str): One of 'low', 'medium', or 'high' (case-insensitive).

    Returns:
        float: Recommended water intake in liters per day.
    """
    # Base water need in milliliters: 35 ml per kg of body weight
    base_ml = weight_kg * 35

    # Map activity level to a multiplier factor:
    #   'low'    → 1.0 (no change)
    #   'medium' → 1.2 (20% increase)
    #   'high'   → 1.4 (40% increase)
    factor = {
        'low': 1.0,
        'medium': 1.2,
        'high': 1.4
    }.get(activity_level.lower(), 1.0)  # default to 1.0 if unrecognized

    # Convert the adjusted volume from milliliters to liters
    return base_ml * factor / 1000