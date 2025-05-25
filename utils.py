def input_float(prompt: str, min_val: float, max_val: float) -> float:
    while True:
        try:
            v = float(input(prompt))
            if min_val <= v <= max_val:
                return v
            print(f"Please input {min_val} to {max_val} number.")
        except ValueError:
            print("Error: Please input a number.")
