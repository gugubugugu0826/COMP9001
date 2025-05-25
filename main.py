from auth import register, login
from calculator import calc_bmi, calc_bmr, calc_water_intake
from utils import input_float


def auth_flow():
    """
    Handle the user authentication loop.

    - Presents a menu to Register, Login, or Exit.
    - On successful login, returns the username.
    - Keeps looping on invalid choice or failed register/login.
    """
    print("== Welcome to Health Assistant ==")
    while True:
        # Prompt user to choose an action
        choice = input("Please choose [1] Register  [2] Login  [3] Exit: ").strip()

        if choice == "1":
            # Call the register function; if successful, loop back to menu
            if register():
                continue      # Registration succeeded; back to auth menu

        elif choice == "2":
            # Call the login function; on success, break out and return user
            user = login()
            if user:
                return user   # Login success → return username to caller

        elif choice == "3":
            # User chose to exit the application
            print("Exit.")
            exit(0)          # Terminate the program immediately

        else:
            # Handle any input that is not 1, 2, or 3
            print("Error: Please input a valid choice.")


def main():
    """
    Main entry point after authentication.

    1. Runs auth_flow() to ensure we have a logged-in user.
    2. Prompts for personal data (weight, height, age, gender, activity level).
    3. Computes BMI, BMR, and recommended daily water intake.
    4. Displays results and a simple health recommendation.
    """
    # 1. Perform login or registration
    user = auth_flow()

    # 2. Greet the user and collect personal metrics
    print(f"\nHello, {user}! === Starting Health Metrics Calculation ===")
    weight   = input_float("Please enter your weight (kg): ", 20, 300)
    height   = input_float("Please enter your height (cm): ", 50, 250)
    age      = int(input_float("Please enter your age (years): ", 5, 120))
    gender   = input("Please enter your gender (male/female): ").strip().lower()
    activity = input("Activity level (low/medium/high): ").strip().lower()

    # 3. Calculate the health metrics
    bmi     = calc_bmi(weight, height)
    bmr     = calc_bmr(weight, height, age, gender)
    water_l = calc_water_intake(weight, activity)

    # 4. Display the results with formatted output
    print(f"\nYour BMI is: {bmi:.1f}")  # One decimal place
    print(f"Your BMR (Basal Metabolic Rate) is approximately: {bmr:.0f} kcal/day")  # No decimals
    print(f"Recommended daily water intake: {water_l:.1f} L")  # In liters

    # 5. Provide a simple recommendation based on BMI category
    if bmi < 18.5:
        print("Recommendation: Underweight — consider increasing nutritional intake.")
    elif bmi < 24:
        print("Recommendation: Healthy weight — maintain your current lifestyle.")
    else:
        print("Recommendation: Overweight — consider increasing exercise and monitoring your diet.")

if __name__ == '__main__':
    main()