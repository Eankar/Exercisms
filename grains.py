def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    if number == 1:
        return 1
    else:
        return 2 * square(number - 1)


def total():
    total_grains = 0

    for i in range(64):
        total_grains += square(i + 1)

    return total_grains