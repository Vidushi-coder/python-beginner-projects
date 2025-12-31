# Password Strength Checker (Python)

This is a **CLI-based Password Strength Checker** built using Python.  
The application allows users to enter a password and checks its strength based on **length and character composition**.

The program also allows users to **check multiple passwords in a single run**.

---

## 🎯 Features

- Checks password strength as **Weak**, **Medium**, or **Strong**
- Supports multiple password checks in one execution
- Uses clear rules based on password composition
- Clean and user-friendly command-line interaction

---

## 🧠 Strength Rules

| Strength | Conditions |
|--------|-----------|
Weak | Length < 6 |
Medium | Contains letters and digits, length ≥ 6 |
Strong | Contains letters, digits, and special characters, length ≥ 8 |

---

## 🧠 Concepts Used

- Functions
- Loops (`while`)
- Conditional statements
- Boolean flags
- String methods (`isalpha()`, `isdigit()`)
- User input handling

---

## ▶️ Sample Output

```
Welcome to Password Strength Checker
You can enter your password here and check its strength

Password please: dghyddg2105@
Password Strength: Strong

Do you want to check the strength of any other password-Yes/No: yes
Password please: abc123
Password Strength: Medium

Do you want to check the strength of any other password-Yes/No: no
Thank you! Please do visit again
```