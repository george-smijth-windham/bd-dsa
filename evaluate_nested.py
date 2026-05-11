operations = {
    "add": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
    "mul": lambda x, y: x * y,
    "pow": lambda x, y: x**y,
}


def evaluate_expression(expr):
    if isinstance(expr, int):
        return expr
    op, left, right = expr
    return operations[op](evaluate_expression(left), evaluate_expression(right))
