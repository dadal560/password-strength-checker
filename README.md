# **Password Strength Checker (Python)**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An open-source tool for **educational and practical purposes**, demonstrating password validation best practices and cybersecurity fundamentals.

## **Security Advisory**
**IMPORTANT**: This project is designed for **learning and security improvement**.
**Best practices:**
* **Always use** strong and unique passwords
* **Never reuse** passwords across multiple services
* **Always enable** two-factor authentication (2FA)
* **Use a professional** password manager
**The author encourages** responsible use of this tool to improve your digital security.

## **Technical Overview**
The checker uses Python regular expressions to:
* Analyze password composition in real-time
* Evaluate character diversity
* Provide personalized recommendations
* Calculate an objective security score

## **Project Structure**

```
password-checker/
│
├── password_checker.py     # Main module
├── test_password_checker.py # Test suite
├── requirements.txt        # Dependencies (none external)
├── .gitignore
├── LICENSE
└── README.md
```

## **Installation and Usage**

### **1. Prerequisites**
* Python 3.6 or higher
* No external dependencies required
* Compatible with Linux, Windows, macOS

### **2. Clone the repository**

```bash
git clone https://github.com/dadal560/password-checker.git
cd password-checker
```

### **3. Create a virtual environment (optional)**

```bash
# Linux/macOS
python3 -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

### **4. Run the checker**

```bash
python password_checker.py
```

### **5. Programmatic usage**

```python
from password_checker import check_character_types

# Analyze a password
check_character_types("MyPassword123!")
```

## **Creating an Executable**

### **Windows (.exe)**

```bash
pip install pyinstaller
pyinstaller --onefile password_checker.py
```

### **Linux (binary)**

```bash
pip install pyinstaller
pyinstaller --onefile password_checker.py
```

The executable will be generated in the `dist/` folder.

## **Features**

### **Current features:**
* Minimum length validation (8 characters)
* Character type analysis (lowercase, uppercase, digits, special characters)
* 4-point scoring system
* Personalized recommendations
* Interactive command-line interface
* Complete test suite with pytest

### **Planned features:**
* Modern graphical interface
* Common password detection
* Entropy analysis
* Have I Been Pwned API integration
* Security report export

## **Security Criteria**

### **Required criteria:**
* **Length**: Minimum 8 characters (recommended: 12+)
* **Lowercase**: At least one letter (a-z)
* **Uppercase**: At least one letter (A-Z)
* **Digits**: At least one number (0-9)
* **Special characters**: At least one symbol `!@#$%^&*(),.?":{}|<>`

### **Rating scale:**
* **Strong (4/4)**: Meets all criteria - Optimal security
* **Medium (2-3/4)**: Some improvements needed
* **Weak (0-1/4)**: Critical vulnerabilities detected

## **Testing and Quality**

### **Run tests**

```bash
# Install pytest (if needed)
pip install pytest

# Run tests
pytest test_password_checker.py -v
```

### **Test coverage:**
* Strong password validation
* Specific weakness detection
* Output message verification
* Edge case testing

## **Security Aspects**

### **Tool security:**
* **No storage**: Passwords are never saved
* **Local processing**: No network transmission
* **Open source**: Security audit possible
* **No logging**: No trace of tested passwords

### **Attack protection:**
1. **Complex passwords** randomly generated
2. **Professional password manager**
3. **Multi-factor authentication** (2FA/MFA)
4. **Regular rotation** of critical passwords
5. **Data breach monitoring**

## **Usage Examples**

### **Weak password:**
```
Please enter a password: 123456
Score: 1/4
Password strength: Weak
Recommendations to improve your password:
- Include at least one lowercase letter.
- Include at least one uppercase letter.
- Include at least one special character.
```

### **Strong password:**
```
Please enter a password: MyS3cur3P@ssw0rd!
Score: 4/4
Password strength: Strong
Your password meets all character type requirements.
```

## **License**
This project is distributed under the MIT License. See the LICENSE file for more information.

## **Author**
**@dadal560**
**Contact:**
* Email: [gwen.henry56@gmail.com]
* GitHub: [@dadal560](https://github.com/dadal560)

## **Useful Links**
* [Python Re Documentation](https://docs.python.org/3/library/re.html)
* [OWASP Password Guidelines](https://owasp.org/www-project-authentication-cheat-sheet/)
* [NIST Password Guidelines](https://pages.nist.gov/800-63-3/)
* [Cybersecurity Best Practices](https://www.cisa.gov/cybersecurity-best-practices)

## **Changelog**

### **Version 1.0.0 (2025-08-22)**
* First functional version
* Complete security criteria validation
* Integrated test suite
* Complete documentation
* Multi-platform support

**Important reminder**: Use this tool to strengthen your digital security and educate on cybersecurity best practices.

### ⭐ If this project was useful to you, don't hesitate to give it a star!
