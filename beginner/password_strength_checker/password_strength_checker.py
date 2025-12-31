print("Welcome to Password Strength Checker")
print("You can enter your password here and chech its strength")

def strength(password):
    Has_Alpha = False
    Has_Digit = False
    Has_Special = False
    
    for i in password:
        if(i.isalpha()):
            Has_Alpha = True
        elif(i.isdigit()):
            Has_Digit = True
        else:
            Has_Special = True
    
    if(len(password)<6):
        return "Weak"
    elif(Has_Alpha and Has_Digit and Has_Special and len(password)>7):
        return "Strong"
    elif(Has_Alpha and Has_Digit and len(password)>5):
        return "Medium"
    else:
        return "Weak"

password=input("Password please: ")
print("Password Strength:",strength(password))

while True:
    another_password = input("\nDo you want to check another password? (yes/no): ")
    if(another_password.lower()=="yes"):
        password=input("Password please: ")
        print("Password Strength:",strength(password))
    else:
        print("Thank you! Please do visit again")
        break