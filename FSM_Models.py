class FSM:
    index = 0

    def next():
        FSM.index += 1

    def error():
        for i in range(FSM.index):
            print(" ")
        print("^")

class dispatchFSM(FSM):
    pass

class numberFSM(FSM):
    pass

class operatorFSM(FSM):
    pass

class IdentifierFSM(FSM):
    pass