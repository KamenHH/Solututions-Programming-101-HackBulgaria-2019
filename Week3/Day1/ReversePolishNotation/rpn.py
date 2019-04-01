def int_or_float(n: float):
    return int(n) if n.is_integer() else n


def _evaluate(op1, op2, operator):
    if operator == '+':
        result =  float(op1) + float(op2)
    elif operator == '-':
        result = float(op1) - float(op2)
    elif operator == '*':
        result = float(op1) * float(op2)
    elif operator == '/':
        result = float(op1) / float(op2)
    return int_or_float(result)

def SQRT(x):
    from math import sqrt
    result = sqrt(float(x))
    return int_or_float(result)

def MAX(stack):
    result = float(max(stack))
    return int_or_float(result)

def MIN(stack):
    result = float(min(stack))
    return int_or_float(result)

def rpn_calculate(expr):
    if len(expr) == 1:
        return int_or_float(float(expr))
    operators = ['+', '-', '*', '/', 'SQRT', 'MAX', 'MIN']
    stack = []
    for char in expr.split(' '):
        if char not in operators:
            stack.append(char)
        elif char == 'SQRT':
            stack.append(SQRT(stack.pop()))
        elif char == 'MAX' or char == 'MIN':
            stack = [MAX(stack)] if char == 'MAX' else [MIN(stack)]
        elif len(stack) >= 2:
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(_evaluate(op1, op2, char))
        elif len(stack) == 1 and char == '-':
            return stack[0]*-1
    return stack[0]

print(rpn_calculate('4 8 + 2 *'))
