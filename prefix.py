def evaluate_prefix(expression):
    stack = []

    tokens = expression.split()[::-1]

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a // b)

    return stack.pop()


expr = "- + * 2 3 * 5 4 9"
print("Prefix Result:", evaluate_prefix(expr))