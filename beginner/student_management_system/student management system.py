print("Welcome to Student Record Management")

def Grade(percentage):
    if(percentage>90):
        return "A+"
    elif(percentage>80):
        return "A"
    elif(percentage>70):
        return "B"
    elif(percentage>60):
        return "C"
    elif(percentage>50):
        return "D"
    else:
        return "E"

def record():
    name = input("\nEnter Student Name: ")

    marks=[]
    math_marks = float(input("Enter Math marks: "))
    marks.append(math_marks)
    science_marks = float(input("Enter Science marks: "))
    marks.append(science_marks)
    english_marks = float(input("Enter English marks: "))
    marks.append(english_marks)
    total = 0
    
    print("\n---RESULT---")
    print("Name:",name)
    
    for i in marks:
        total+=i
    print("Total:",total)
    
    percentage = ((total/300)*100)
    print("Percentage:",round(percentage,2),"%")
    
    print("Grade:", Grade(percentage))

record()

while True:
    another_record = input("\nDo you want to enter the result of any other student? (yes/no): ")
    if(another_record.lower()=="yes"):
        record()
    else:
        print("Thank you!")
        break