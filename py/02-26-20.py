"""
This problem was asked by Facebook.

Given a string consisting of parentheses, single digits, and positive and negative signs, convert the string into a mathematical expression to obtain the answer.

Don't use eval or a similar built-in parser.

For example, given '-1 + (2 + 3)', you should return 4.

1 + 2      = 3
-1 + -1    = -2
-(-1) - -1 = 2

Strategy:
    1. Parse input into individual elements (paren, digit, etc.)
    2. Group tokens by paren
    3. Apply signage (-1, ----1)
    4. Wrap entire algorithm inside parens
    5. Recursively perform mathematical operations within each paren group
"""

from pprint import pprint

class Token:
    def __repr__(self):
        attrs = ', '.join(
            f'{key}={repr(val)}'
            for key, val in
            self.__dict__.items()
            if not key.startswith('__')
        )
        return f'{self.__class__.__name__}({attrs})'

class Digit(Token):
    def __init__(self, val):
        self.val = val

class Operator(Token):
    def __init__(self, op):
        self.op = op

class OpenParen(Token):
    pass

class CloseParen(Token):
    pass



def math(src):
    src = f'({src})'

    tokens = []
    for char in src:
        if char in '()':
            tokens.append(OpenParen() if char == '(' else CloseParen())
        elif char in '0123456789':
            tokens.append(Digit(val=char))
        elif char in '+-*/':
            tokens.append(Operator(op=char))

    # print()
    # pprint(tokens)
    # print()
    
    stack = []
    sign = []
    for token in tokens:
        if isinstance(token, OpenParen):
            stack.append([])
        elif isinstance(token, CloseParen):
            paren = stack.pop()
            if stack:
                stack[-1].append(paren)
            else:
                stack.extend(paren)
        elif isinstance(token, Digit):
            while sign:
                token.val = str(int(sign.pop().op + token.val))
            if stack[-1] and isinstance(stack[-1][-1], Digit):
                stack[-1][-1].val += token.val
            else:
                stack[-1].append(token)
        elif isinstance(token, Operator) and token.op in '+-':
            if not stack[-1] or (stack and isinstance(stack[-1][-1], Operator)):
                sign.append(token)
            else:
                stack[-1].append(token)
        else:
            stack[-1].append(token)

    # print()
    # pprint(stack)
    # print()

    def evaluate(expr):
        terms = iter(expr)
        value = int(next(terms).val)
        while terms.__length_hint__():
            op, b = next(terms), next(terms)

            if isinstance(b, list):
                b = Digit(evaluate(b))

            if op.op == '+':
                value += int(b.val)
            elif op.op == '-':
                value -= int(b.val)
            elif op.op == '*':
                value *= int(b.val)
            elif op.op == '/':
                value /= int(b.val)

        return value

    # print()
    # print(evaluate(stack))
    # print()

if __name__ == '__main__':
    math('10 + -20 + (-30 + +40)')
    math('-1 + (2 + 3)')
