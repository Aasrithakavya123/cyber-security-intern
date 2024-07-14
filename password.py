import re

def assess_password_strength(password):
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None
    
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"
    
    feedback = {
        "length": "Password must be at least 8 characters long." if not length_criteria else "Length is sufficient.",
        "uppercase": "Password must contain at least one uppercase letter." if not uppercase_criteria else "Contains uppercase letter.",
        "lowercase": "Password must contain at least one lowercase letter." if not lowercase_criteria else "Contains lowercase letter.",
        "digit": "Password must contain at least one digit." if not digit_criteria else "Contains digit.",
        "special_char": "Password must contain at least one special character." if not special_char_criteria else "Contains special character."
    }
    
    return strength, feedback

def main():
    password = input("Enter a password to assess: ").strip()
    strength, feedback = assess_password_strength(password)
    
    print(f"Password Strength: {strength}")
    print("Feedback:")
    for criterion, message in feedback.items():
        print(f"- {message}")

if __name__ == "__main__":
    main()
