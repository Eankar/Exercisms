def encode(message, rails):
    encoded_message = []
    encoded_message_string = ""
    num_top_dots = rails * 2 - 3
    rail_num = 1
    more_dots = False
    going_down = True

    while rail_num <= rails:
        index = 0
        while index < len(message):
            try:
                if rail_num == 1: # Top rail
                    # if index != 0:
                    #     for i in range(num_top_dots):
                    #         encoded_message.append(".")
                    encoded_message.append(message[index])
                    index += num_top_dots + 1
                elif rail_num == rails: # Bottom rail
                    index += rail_num - 1
                    # if index == rail_num -1 or index >= len(message):
                    #     for i in range(rails-1):
                    #         encoded_message.append(".")
                    # else:
                    #     for i in range(rails):
                    #         encoded_message.append(".")
                    encoded_message.append(message[index])
                    index += rail_num - 1
                else: # Middle rails
                    index += num_top_dots - 2
                    if index != rails
                    -1:
                        encoded_message.append(message[index])
                    
            except:
                pass
            
        rail_num += 1
        more_dots = not more_dots
        going_down = not going_down

    for i in encoded_message:
        encoded_message_string += i
    
    return encoded_message_string


def decode(encoded_message, rails):
    pass

print(encode("WEAREDISCOVEREDFLEEATONCE", 3))
#print(encode("ESXIEECSR", 4))

#1 if 2 rails
#3 if 3 rails
#5 if 4 rails
#7 if 5 rails
#9 if 6 rails

#rails * 2 - 3
#lower dots = top dots - 2 until bottom row

#1.........1...........................................
#.2.......2.2............................................
#..3.....3...3...........................................
#...4...4.....4..........................................
#....5.5.......5.........................................
#.....6.........6.......................................

#1.1.1
#.2.2.

#1...1
#.2.2.
#..3..

#ESXIEECSR

#E....C..
#.S..E.S.
#..X.E..R
#...I.....


# def encode(message, rails):
#     message_list = []
#     encoded_message = []

#     for i in message:
#         message_list.append(i)
    
#     #print(f"Message_List: {message_list}")

#     for i in range(len(message_list)):
#         try:
#             #print("Got Here")
#             encoded_message.append(message_list.pop(i))
#             i += rails
#         except:
#             pass
    
#     print(encoded_message)


# encode("WEAREDISCOVEREDFLEEATONCE", 3)

#EAREDISCOVEREDFLEEATONCE
