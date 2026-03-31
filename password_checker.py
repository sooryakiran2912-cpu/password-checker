import re

def check_password_strength(password):
    # Criteria
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    # Evaluate strength
    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = errors.count(False)

    # Output
    if score == 5:
        strength = "Very Strong"
    elif score >= 3:
        strength = "Strong"
    elif score >= 2:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength

# Main
if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result = check_password_strength(pwd)
    print(f"Password Strength: {result}")
