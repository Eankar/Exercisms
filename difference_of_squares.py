def square_of_sum(number):
    num = 1
    sum = 0
    while num <= number:
        sum += num
        num += 1

    return sum ** 2


def sum_of_squares(number):
    num = 1
    sum = 0
    while num <= number:
        sum += num ** 2
        num += 1

    return sum


def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)