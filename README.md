# Health Assistant

A command-line health assistant tool for user registration/login and calculation of common health metrics, including:

* **BMI** (Body Mass Index)
* **BMR** (Basal Metabolic Rate, using the Mifflin-St Jeor equation)
* **Daily Water Intake Recommendation**

## Features

* User registration & login (username + SHA-256 password hashing)
* Secure password input (hidden input)
* Input validation (range checking)
* Automatic calculation and formatted output of health metrics
* Simple health suggestions based on BMI


## Usage

Run the application:

```bash
python main.py
```

1. After launching, choose:

   * `[1]` Register
   * `[2]` Login
   * `[3]` Exit
2. After registering or logging in, enter the following inputs:

   * Weight (kg)
   * Height (cm)
   * Age (years)
   * Gender (male/female)
   * Activity level (low/medium/high)
3. View the calculated results:

   * BMI value
   * BMR (daily basal metabolic rate)
   * Recommended daily water intake (L)
   * Simple health advice

## Project Structure

```text
health-assistant/
├── main.py        # Application entry point
├── auth.py        # User registration and login
├── calculator.py  # BMI, BMR, and water intake calculations
├── utils.py       # Input validation helper functions
├── users.json     # User data storage file
└── README.md      # Project documentation
```

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License – see the [LICENSE](LICENSE) file for details.
