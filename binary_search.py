def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")
        
    index = len(search_list) // 2

    if search_list[index] == value:
        return index
    elif search_list[index] > value: #Look on left half
        return find(search_list[:index], value)
    elif search_list[index] < value: #Look on right half
        return index + find(search_list[index+1:], value) + 1
    else:
        raise ValueError("value not in array")