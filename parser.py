from lexer import Lexer

class Node:
    pass

class BinOp(Node):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class Num(Node):
    def __init__(self, value):
        self.value = value

class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = lexer.get_next_token()

    def error(self):
        raise Exception('Invalid syntax')

    def eat(self, token_type):
        if self.current_token[0] == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        if token[0] == 'INTEGER':
            self.eat('INTEGER')
            return Num(token[1])
        elif token[0] == 'LPAREN':
            self.eat('LPAREN')
            node = self.expr()  # Recursive call to parse the expression inside parentheses
            self.eat('RPAREN')
            return node

    def term(self):
        node = self.factor()
        while self.current_token[0] in ('MUL', 'DIV'):
            token = self.current_token
            if token[0] == 'MUL':
                self.eat('MUL')
            elif token[0] == 'DIV':
                self.eat('DIV')
            node = BinOp(node, token[1], self.factor())
        return node

    def expr(self):
        node = self.term()
        while self.current_token[0] in ('PLUS', 'MINUS'):
            token = self.current_token
            if token[0] == 'PLUS':
                self.eat('PLUS')
            elif token[0] == 'MINUS':
                self.eat('MINUS')
            node = BinOp(node, token[1], self.term())
        return node