def steps(number):
    if number < 1 or not type(number) == int:
        raise ValueError("Only positive integers are allowed")
    
    num_steps = 0
    num = number

    while num != 1:
        if num %2 == 0:
            num = num / 2
            num_steps += 1
        else:
            num = num * 3 + 1
            num_steps += 1

    return num_steps