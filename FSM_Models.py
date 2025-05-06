class FSM:
    index = 0

    def next(self):
        FSM.index += 1

    def error(self):
        for i in range(FSM.index):
            print(" ", end="")
        print("^")

class dispatchFSM(FSM):
    pass

class numberFSM(FSM):
    pass

class operatorFSM(FSM):
    pass

class IdentifierFSM(FSM):
    pass