"""
Implement Lexer
    Implement Dispatcher FSM
    Implement Integer FSM
    Implement Operator FSM
    Implement Identifier FSM (for non-operator/noninteger inputs such as sin, cos, log, etc)

Implement Parser
    Conduct further research as to the elements of a parser

Implement an executor for parsed expression
    Implement ATS
    Implement Tree Navigator
    Ensure Executor's conformity to Arithmetical rules
"""

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