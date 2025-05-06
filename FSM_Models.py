class dispatchFSM:
    index = 0

    def next(self):
        dispatchFSM.index += 1

    def error(self):
        for i in range(dispatchFSM.index):
            print(" ", end="")
        print("^")

class numberFSM(dispatchFSM):
    pass

class operatorFSM(dispatchFSM):
    pass

class IdentifierFSM(dispatchFSM):
    pass