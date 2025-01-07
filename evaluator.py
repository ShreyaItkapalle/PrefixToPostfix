# evaluator.py

def is_operator(c):
    return c in "+-*/^"

def prefix_to_postfix(expression):
    # Reverse the prefix expression
    expression = expression.split()
    expression.reverse()
    
    stack = []
    
    for symbol in expression:
        if not is_operator(symbol):
            stack.append(symbol)
        else:
            # Operator: Pop two operands, combine them, and push back to stack
            op1 = stack.pop()
            op2 = stack.pop()
            stack.append(op1 + ' ' + op2 + ' ' + symbol)
    
    return stack[-1]
