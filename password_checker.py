import re

def ask_password():
    password = input("Please enter a password: ")

    while not password or len(password) < 8:
        if not password:
            print("Error: password cannot be empty.")
        elif len(password) < 8:
            print("Error: password must be at least 8 characters long.")
        password = input("Please enter a password: ")

    return password

def check_character_types(password):
    recommendations = []
    score = 4
    SPECIAL_CHARS = r"!@#$%^&*(),.?\":{}|<>"
    if not re.search(r"[a-z]", password):
        score -= 1
        recommendations.append("Include at least one lowercase letter.")
    if not re.search(r"[A-Z]", password):
        score -= 1
        recommendations.append("Include at least one uppercase letter.")
    if not re.search(r"[0-9]", password):
        score -= 1
        recommendations.append("Include at least one digit.")
    if not re.search(f"[{re.escape(SPECIAL_CHARS)}]", password):
        score -= 1
        recommendations.append("Include at least one special character.")
    print(f"Score: {score}/4")
    if score == 4:
        print("Password strength: Strong")
    elif score >= 2:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")
        
    if recommendations:
        print("Recommendations to improve your password:")
        for recommendation in recommendations:
            print(f"- {recommendation}")
    else:        
        print("Your password meets all character type requirements.")
        
if __name__ == "__main__":
    result = ask_password()
    check_character_types(result)
    print(f"Password : {result}")
