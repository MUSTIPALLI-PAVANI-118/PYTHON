def evaluate_postfix(expression):
    stack=[]
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            b=stack.pop()
            a=stack.pop()

            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                stack.append(a // b)
    return stack.pop()

expr ="2 3 * 5 4 * + 9 -"
print("postfix result:",evaluate_postfix(expr))