
import arithmetic

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b



num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", arithmetic.add(num1, num2))
print("Subtraction:", arithmetic.sub(num1, num2))
print("Multiplication:", arithmetic.mult(num1, num2))
print("Division:", arithmetic.div(num1, num2))