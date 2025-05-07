class dispatchFSM:
    index = 0 # Global FSM class and child class variable to track current position in input string
    
    
    
    def next(self):
        """Increases the current index by 1 if the current index is not the last index."""
        #if index < string.size()
        dispatchFSM.index += 1

    def error(self):
        """Outputs the currently known equaiton with an arrow under the index of error."""
        for i in range(dispatchFSM.index):
            print(" ", end="")
        print("^")

class numberFSM(dispatchFSM):
    pass

class operatorFSM(dispatchFSM):
    pass

class IdentifierFSM(dispatchFSM):
    pass