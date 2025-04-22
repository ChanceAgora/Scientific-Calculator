def main():
    x = input().split()

    valStack = []
    opStack = []

def parentheses(valStack, opStack):
    """Evaluates all operations in a parenthetical expression and stops at the opening parenthesis. Removes opening paren from the operator stack."""
    while(len(opStack) > 0 and not opStack[-1] == '('): #Ensures the operator stack has at least one element and stops when an opening paren is found
        operate(valStack, opStack)
    opStack.pop() #Removes opening paren

    
def operate(valStack, opStack):
    """Executes the operator from the top of the operator stack on the top two values from the value stack."""
    if(opStack[-1] == '^'):
        valStack[-2] = valStack[-2] ** valStack[-1]
    elif(opStack[-1] == '*'):
        valStack[-2] = valStack[-2] * valStack[-1]
    elif(opStack[-1] == '/'):
        valStack[-2] = valStack[-2] / valStack[-1]
    elif(opStack[-1] == '+'):
        valStack[-2] = valStack[-2] + valStack[-1]
    elif(opStack[-1] == '-'):
        valStack[-2] = valStack[-2] - valStack[-1]
    # Remove used value and used operator
    opStack.pop()
    valStack.pop()

def stackPriority(opStack, op) -> bool:
    """Returns true if the top of the stack takes precedence in the order of operations compared to the compared operator. Returns false if stack is empty or does not take precedent."""
    if(len(opStack) == 0): return False
    elif(opPrecedence(opStack[-1]) >= opPrecedence(op)): return True
    else: return False
    
def opPrecedence(op):
    """Outputs values associated with operator symbols in accordance with the order of operations. """
    if(op == '('): op = 4
    elif(op == '^'): op = 3
    elif(op == '*' or '/'): op = 2
    elif(op == '+' or '-'): op = 1
    else: op = None

def rightAssociative(op) -> bool:
    """Returns true if the given operator is right associative. False otherwise."""
    if(op == '^'): return True
    return False


main()