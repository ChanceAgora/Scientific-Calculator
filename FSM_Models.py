class FSM:
    index = 0

    def __init__(self):
        FSM.index += 1
            
    def __str__(self):
        return f"{FSM.index}"

class dispatchFSM(FSM):
    pass

class numberFSM(FSM):
    pass

class operatorFSM(FSM):
    pass

class IdentifierFSM(FSM):
    pass