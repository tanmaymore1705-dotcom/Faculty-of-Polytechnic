def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Cannot modulo by zero"
    return a % b


# Example
a = 10
b = 5

print("Add:", add(a, b))
print("Subtract:", subtract(a, b))
print("Multiply:", multiply(a, b))
print("Divide:", divide(a, b))
print("Modulo:", modulo(a, b))
