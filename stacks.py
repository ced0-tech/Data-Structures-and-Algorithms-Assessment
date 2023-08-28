def is_balanced(expression):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    for char in expression:
        if char in brackets.keys():  # If it's an opening bracket
            stack.append(char)
        elif char in brackets.values():  # If it's a closing bracket
            if not stack or brackets[stack.pop()] != char:
                return False
    
    return not stack  # If stack is empty, expression is balanced

# Test cases
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  # Output: True
print(is_balanced(expression2))  # Output: False

    