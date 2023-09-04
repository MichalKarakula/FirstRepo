def flatten_list(input_list):
    flattened = []
    stack = [input_list]

    while stack:
        current = stack.pop()
        for item in current:
            if isinstance(item, list):
                stack.append(item)
            elif isinstance(item, int):
                flattened.append(item)

    return flattened


