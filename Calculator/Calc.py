def Addition(a,b):
    print("Sum of the number is: ",a+b)

def Subtraction(a,b):
    print("Difference of the number is: ",a-b)

def Multiplication(a,b):
    print("Product of the number is: ",a*b)

def Division(a,b):
    print("Ratio of the number is: ",a/b)

def Power(a,b):
    print(f"{a} to the power {b} is: ",a**b)

if __name__ == '__main__':
    a = int(input("Enter a number: \n"))
    op =input("Enter the operator: \n")
    b = int(input("Enter a number: \n"))
    if op=="+":
        Addition(a,b)
    if op=="-":
        Subtraction(a,b)
    if op=="*":
        Multiplication(a,b)
    if op=="/":
        Division(a,b)
    if op=="**":
        Power(a,b)