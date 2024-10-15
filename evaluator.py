from parser import Parser, Num, BinOp  # Importing Num and BinOp
from lexer import Lexer  # Importing Lexer

class Evaluator:
    def visit(self, node):
        if isinstance(node, Num):
            return node.value
        elif isinstance(node, BinOp):
            if node.op == '+':
                return self.visit(node.left) + self.visit(node.right)
            elif node.op == '-':
                return self.visit(node.left) - self.visit(node.right)
            elif node.op == '*':
                return self.visit(node.left) * self.visit(node.right)
            elif node.op == '/':
                return self.visit(node.left) / self.visit(node.right)

def main():
    while True:
        try:
            text = input("Enter an expression: ")
            lexer = Lexer(text)  # Create a lexer instance
            parser = Parser(lexer)
            tree = parser.expr()
            evaluator = Evaluator()
            result = evaluator.visit(tree)
            print(f"Result: {result}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    main()