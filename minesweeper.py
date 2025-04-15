def annotate(minefield):
    if len(minefield) < 1:
        raise ValueError("The board is invalid with current input.")
    
    minefield = [list(row) for row in minefield]

    for i, rows in enumerate(minefield):
        column, row, num = 0

        for x, columns in enumerate(rows):
            if x == " ":
                try:
                    if minefield[i][x - 1] == "*":
                        num += 1
                    if minefield[i][x + 1] == "*":
                        num += 1
                    if minefield[i + 1][x] == "*":
                        num += 1
                    if minefield[i - 1][x] == "*":
                        num += 1
                    if minefield[i - 1][x - 1] == "*":
                        num += 1
                    if minefield[i + 1][x - 1] == "*":
                        num += 1
                    if minefield[i - 1][x + 1] == "*":
                        num += 1
                    if minefield[i + 1][x + 1] == "*":
                        num += 1
                except IndexError:
                    pass
                minefield[i][x] = str(num)     

    return ["".join(row) for row in minefield]   






    #Get dimensions
    # height = len(minefield)
    # width = len(minefield[0])
    # for i in minefield:
    #     num = ""
    #     for x in i:
    #         if x != "*":
    #             if x > 1:
    #                 if x - 1 == "*":
    #                     num += 1
    #             if x < len(i) - 1:
    #                 if x + 1 == "*":
    #                     num += 1
    #             if i < len(minefield) - 1:
    #                 if x > 1:
    #                     if minefield[i + 1][x - 1] == "*":
    #                         num += 1
    #                 if x < len(i) - 1:
    #                     if minefield[i + 1][x + 1] == "*":
    #                         num += 1

        

minefield = ["  *  ", "  *  ", "*****", "  *  ", "  *  "]
print(len(minefield))
for i in minefield:
    print(f"{i}\n")
print("Break")
print(minefield[0][2])