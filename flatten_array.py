def flatten(iterable):
    output = []

    if not isinstance(iterable, list):
        return output  # If input isn't a list, return empty list

    for item in iterable:
        if item is None:
            continue
        elif isinstance(item, list):
            output.extend(flatten(item))  # Recursively flatten
        else:
            output.append(item)

    return output