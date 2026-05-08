from stack import Stack


def is_balanced(input_str):
    stack = Stack()
    for parenthesis in input_str:
        if parenthesis == "(":
            stack.push(parenthesis)
            continue
        if parenthesis == ")":
            if stack.size():
                stack.pop()
            else:
                return False

    return stack.size() == 0
