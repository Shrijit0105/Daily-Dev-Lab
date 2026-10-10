def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

def root( a, b):
    if b == 0:
        raise ValueError("root degree cannot be zero.")
    return a ** (1 / b)    

def operation(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return subtract(a, b)
    elif op == '*':
        return multiply(a, b)
    elif op == '/':
        return divide(a, b)
    elif op == '**':
        return power(a, b)
    elif op == 'root':
        return root(a, b)
    else:
        raise ValueError("Invalid operation.")



input_a = int(input("Enter the first number: "))
input_b = int(input("Enter the second number: "))
input_op = input("Enter the operation (+, -, *, /, **, root): ")
result = operation(input_a, input_b, input_op)
print(f"The result of {input_a} {input_op} {input_b} is: {result}")        
            