def is_valid_password(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)

    return has_lower and has_upper and has_digit

# Get password input from the user
user_password = input("Enter your password: ")

if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password must contain at least one lowercase letter, one uppercase letter, and one number.")
