import enum

def main():
    x = Token(TokenType.NUMBER, 3.14159)
    print(x)

class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value
    
    def __str__(self):
        return f"{self.type.name}({self.value})"
        
class TokenType(enum.Enum):
    NUMBER = "NUMBER"
    OPERATOR = "OPERATOR"
    IDENTIFIER = "IDENTIFIER"

OPERATORS = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "^": lambda a, b: a ** b
}


main()