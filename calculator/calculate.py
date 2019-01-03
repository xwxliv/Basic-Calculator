def doCal(first, op, second):
    if op == '+' or op == '&plus':
        return int(first) + int(second)
    elif op == '-' or op == '&minus':
        return int(first) - int(second)
    elif op == '×' or op == '&times':
        return round(int(first) * int(second))
    return round(int(first) / int(second))
