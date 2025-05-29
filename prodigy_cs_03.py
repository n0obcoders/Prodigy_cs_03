import re

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append(" Add at least one uppercase letter.")

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append(" Include at least one number.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback.append(" Add at least one special character.")

    
    if strength == 5:
        rating = " Very Strong"
    elif strength == 4:
        rating = " Strong"
    elif strength == 3:
        rating = "️ Medium"
    else:
        rating = " Weak"

    return rating, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")
    rating, feedback = check_password_strength(password)

    print("\nPassword Strength:", rating)
    if feedback:
        print("\nSuggestions to improve:")
        for msg in feedback:
            print("-", msg)

if __name__ == "__main__":
    main()
