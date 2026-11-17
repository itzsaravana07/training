fruits={"apple","mango","banana","grapes"}
fruits.add("orange")
print(fruits)
fruits.remove("banana")
print(fruits)



student={
    'dept': 'Computer Science',
    'name': 'Aaditya',
    "age": 19,
    "marks": 85
}
student["fiancée"] = "fiancee illa"
student.pop("fiancée")
student["height"] = 6.0
student["weight"] = 76
student["relationship"] = "married"
print(list(student.values()))
print(list(student.keys()))
for key,values in student.items():
    print(key,":",values)

marks=[85, 90, 78, 92, 88]
print(max(marks[0:2]))
print(marks[::-1])



def add_numbers(num1,num2):
    return num1+num2
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))
result=add_numbers(num1,num2)
print(f"The sum of {num1} and {num2} is: {result}")   

def calc(a,b):
    return a+b,a-b,a*b,a/b
total,sub,mul,div=calc(10,5)
print("Total:", total)
print("Subtraction:", sub)
print("Multiplication:", mul)
print("Division:", div)

def student_info(name, age, dept):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Department: {dept}")
student_info("Aaditya", 19, "Computer Science")

