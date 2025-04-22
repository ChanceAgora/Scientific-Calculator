def main():
    x = input().split()
    print(x)

    valStack = []
    opStack = []
    

def stackPriority(stackOp, op) -> bool:
    if(opPrecedence(stackOp) >= opPrecedence(op)): return True
    else: return False
    
def opPrecedence(op):
    if(op == '^'): op = 3
    elif(op == '*' or '/'): op = 2
    elif(op == '+' or '-'): op = 1
    elif(op == '('): op = 0
    else: op = None

#def right_associative():
    # calculate right associative operands like ^(power)

#def parentheses():
    # calculate all operands until parentheses set is resolved
    # will begin when a closing parentheses is found and terminate when an opening parentheses is found
    # this way a parenthetical expression will be entirely evaluated before continuing

main()