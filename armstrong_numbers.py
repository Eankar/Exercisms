def is_armstrong_number(number):
    sum = 0
    for i in list(str(number)):
        sum += int(i) ** len(list(str(number)))

    return sum == number