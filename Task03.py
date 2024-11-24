import re

def password_strength(password):
    """Assess the strength of a password based on specific criteria."""

    # Criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Score calculation
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria,
                 number_criteria, special_criteria])

    # Feedback
    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Moderate"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "length_criteria": length_criteria,
        "uppercase_criteria": uppercase_criteria,
        "lowercase_criteria": lowercase_criteria,
        "number_criteria": number_criteria,
        "special_criteria": special_criteria,
        "strength": strength,
    }


# Test the function
if __name__ == "__main__":
    password = input("Enter a password to assess: ")
    result = password_strength(password)

    print("\nPassword Assessment:")
    print(f"Length Criteria Met: {result['length_criteria']}")
    print(f"Uppercase Criteria Met: {result['uppercase_criteria']}")
    print(f"Lowercase Criteria Met: {result['lowercase_criteria']}")
    print(f"Number Criteria Met: {result['number_criteria']}")
    print(f"Special Character Criteria Met: {result['special_criteria']}")
    print(f"Password Strength: {result['strength']}")
