# Student Result Report :

# 1. Ask the user to enter student details: Name, Roll Number, and Class.
# 2. Take marks of five subjects (out of 100): English, Mathematics, Science, Computer, Social
# Studies.
# 3. Calculate Total Marks and Percentage.
# 4. Result Rules:
# • If any subject marks are below 35, result is FAIL.
# • Otherwise, result is PASS.
# 5. Grade Calculation (only if PASS):
# • 90% and above – Grade A
# • 75% to 89% – Grade B
# • 50% to 74% – Grade C
# • Below 50% – Grade D
# 6. If result is FAIL, display Grade as 'No Grade'.

# Ask the user to enter Name, Roll no and class :

Name = input("Enter Student Name:")
Roll_no = int(input("Enter Student Roll_no:"))
Student_Class = input("Enter Student Class:")


# Take marks of five subjects :

english = int(input("Enter English Marks:"))
maths = int(input("Enter Maths Marks:"))
science = int(input("Enter Science Marks:"))
Computer = int(input("Enter Computer Marks:"))
Social_studies = int(input("Enter Social_studies Marks:"))


# Calculate Total marks and percentage :

total_marks = english + maths + science + Computer + Social_studies
percentage = (total_marks/500) * 100

# Result Check :

if english < 35 or maths < 35 or science < 35 or Computer < 35 or Social_studies < 35:
    print("FAIL")
else:
    result = "PASS"
    if percentage >= 90:
        Grade = "A"
    elif percentage >= 75:
        Grade = "B"
    elif percentage >= 50:
        Grade = "C"
    else:
        Grade = "D"

# Result or Output :
print(" ")
print("Name:",Name)
print("Roll_no:",Roll_no)
print("Student_class:",Student_Class)
print(" ")
print("English :", english)
print("Maths :", maths)
print("Science :", science)
print("Computer :", Computer)
print("Social :", Social_studies)
print(" ")
print("Total Marks :", total_marks, "/ 500")
print(f"Percentage : {percentage:.2f} %")
print("Result :", result)
print("Grade :", Grade)