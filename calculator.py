def main():
    x = input().split()
    print(x)

    valStack = []
    opStack = []
    

def stackPriority(opStack, op) -> bool: # Return true if the stack operator needs to be executed, return false if add current operator to stack
    if(len(opStack) == 0): return False
    elif(opPrecedence(opStack[-1]) >= opPrecedence(op)): return True
    else: return False
    
def opPrecedence(op):
    if(op == '('): op = 4
    elif(op == '^'): op = 3
    elif(op == '*' or '/'): op = 2
    elif(op == '+' or '-'): op = 1
    else: op = None

# def right_associative():
    # calculate right associative operands like ^(power)

# def parentheses(valStack, opStack):
   #  while(not opStack[-1] == '('): 

def operate(valStack, opStack):
    if(opStack[-1] == '^'):
        valStack[-2] = valStack[-2] ** valStack[-1]
        opStack.pop()
        valStack.pop()
    elif(opStack[-1] == '*'):
        valStack[-2] = valStack[-2] * valStack[-1]
        valStack.pop()
        opStack.pop()
    elif(opStack[-1] == '/'):
        valStack[-2] = valStack[-2] / valStack[-1]
        valStack.pop()
        opStack.pop()
    elif(opStack[-1] == '+'):
        valStack[-2] = valStack[-2] + valStack[-1]
        valStack.pop()
        opStack.pop()
    elif(opStack[-1] == '-'):
        valStack[-2] = valStack[-2] - valStack[-1]
        valStack.pop()
        opStack.pop()

main()