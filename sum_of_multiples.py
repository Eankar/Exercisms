def sum_of_multiples(limit: int, multiples: list[int]):
    nums_to_add = set()
    for value in multiples:
        if value > 0:
            nums_to_add.update(range(value, limit, value))
            
    return sum(nums_to_add)