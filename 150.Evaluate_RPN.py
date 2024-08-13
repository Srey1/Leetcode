def evalRPN(self, tokens: List[str]) -> int:
    stack = []
    for i in tokens:
        if i == "+":
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif i == "-":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)
        elif i == "*":
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif i == "/":
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(num2 / num1))
        else:
            stack.append(int(i))
    return stack.pop()