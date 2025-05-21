# Implementation Checklist
# NumberFSM States and lexing functionality
# OperatorFSM States and lexing functionality
# IdentifierFSM States and lexing functionality
# DispatchFSM lexing Functionality

class DispatchFSM:
    index = 0 # Global FSM class and child class variable to track current position in input string
    tokens = [] # List for storing and updating each unique token in input

    def __init__(self):
        self.state = "START"
    
    def lexInput(equation) -> list:
        """(Not yet Implemented)\n
        Takes a string input and returns a list of all valid tokens from that string.\n
        Returns an error if there are invalid inputs present."""

        # Loop until last index is evaluated
            # Check current character
            # Pas int to NumberFSM
            # Pass operation symbol to OperatorFSM
            # Pass anything else to IdentifierFSM

    
    def next(self):
        """Increases the current index by 1 if the current index is not the last index."""
        #if index < string.size()
        DispatchFSM.index += 1

    def error(self):
        """Outputs the currently known equaiton with an arrow under the index of error."""
        for i in range(DispatchFSM.index):
            print(" ", end="")
        print("^")

class NumberFSM(DispatchFSM):
    def __init__(self):
        super()
        self.decimalValue = 0.1 # Used to properly add numbers from the input string to the correct number place after a decimal (divide by 10 for all subsequent numbers after 0.x, i.e. 0.01, 0.001, etc.)
    
    def lexChar(self, equation):
        isNegative = False
        bufferNum = 0
        for DispatchFSM.index in range(equation.size() + 1):
            if DispatchFSM.index == equation.size():
                self.state = "START"
                DispatchFSM.tokens.append(bufferNum)
            elif self.state == "START":
                match equation:
                    case '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '0':
                        bufferNum += int(equation[DispatchFSM.index])
                        break
                    case '.':
                        self.state = "DECIMAL"
                        break
                    case '-':
                        isNegative = True
                        break
                

class OperatorFSM(DispatchFSM):
    pass

class IdentifierFSM(DispatchFSM):
    pass