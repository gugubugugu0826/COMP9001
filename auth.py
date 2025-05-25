import json, os, hashlib, getpass

# Path to the JSON file storing username: password_hash pairs
USERS_FILE = "users.json"

def load_users() -> dict:
    """
    Load existing users from the JSON file.

    Returns:
        dict: A dictionary mapping usernames to hashed passwords.
              If file does not exist, returns an empty dictionary.
    """
    # Check if the users file exists; if not, return an empty dict
    if not os.path.exists(USERS_FILE):
        return {}
    # Open the file in read mode and parse JSON into a dict
    with open(USERS_FILE, "r") as f:
        return json.load(f)


def save_users(users: dict):
    """
    Save the users dictionary to the JSON file.

    Args:
        users (dict): Mapping of usernames to hashed passwords.
    """
    # Open the users file in write mode, overwrite its contents
    with open(USERS_FILE, "w") as f:
        # Use ensure_ascii=False to support Unicode, indent=2 for readability
        json.dump(users, f, ensure_ascii=False, indent=2)


def hash_password(pwd: str) -> str:
    """
    Generate a SHA-256 hash for the given password string.

    Args:
        pwd (str): The plaintext password.

    Returns:
        str: The hexadecimal SHA-256 hash of the password.
    """
    # Encode the password to bytes using UTF-8, hash it, and return hex digest
    return hashlib.sha256(pwd.encode("utf-8")).hexdigest()


def register() -> bool:
    """
    Register a new user by prompting for username and password.

    Returns:
        bool: True if registration succeeded, False otherwise.
    """
    # Load existing users from file
    users = load_users()
    # Prompt user for a username and strip whitespace
    username = input("Please input username:").strip()
    # Check if username already exists
    if username in users:
        print("Username already registered.")
        return False
    # Prompt for password securely (no echo) and confirm it
    pwd1 = getpass.getpass("Please input password:")
    pwd2 = getpass.getpass("Please confirm password:")
    # Ensure both entries match
    if pwd1 != pwd2:
        print("Passwords do not match.")
        return False
    # Hash the password and store in the users dictionary
    users[username] = hash_password(pwd1)
    # Save the updated users dict back to the JSON file
    save_users(users)
    print("Registered.")
    return True


def login() -> str | None:
    """
    Authenticate an existing user by verifying username and password.

    Returns:
        str: The username if login succeeds.
        None: If login fails (username not found or incorrect password).
    """
    # Load current users from JSON
    users = load_users()
    # Prompt for username and strip whitespace
    username = input("Username:").strip()
    # Check if username exists in the users dict
    if username not in users:
        print("Username not found.")
        return None
    # Prompt for password securely (hidden input)
    pwd = getpass.getpass("Password:")
    # Compare stored hash with hash of the entered password
    if users[username] != hash_password(pwd):
        print("Password incorrect.")
        return None
    # Login successful; greet the user and return the username
    print(f"Login Success! {username}!")
    return username