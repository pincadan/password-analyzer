import re

def analyze_password(password):
    # Check password length
    if len(password) < 8:
        return "Your password is too short. It should be at least 8 characters long."
    
    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Your password should contain at least one uppercase letter."
    
    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Your password should contain at least one lowercase letter."
    
    # Check for digits
    if not re.search(r'\d', password):
        return "Your password should contain at least one digit."
    
    # Check for special characters
    if not re.search(r'[@_!#$%^&*()<>?/\|}{~:]', password):
        return "Your password should contain at least one special character."
    
    return "Your password is strong!"

# Example usage
password = input("Enter your password: ")
result = analyze_password(password)
print(result)