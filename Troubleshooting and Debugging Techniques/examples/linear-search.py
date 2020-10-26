def linear_search(list, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    for i, item in enumerate(list):
        if item == key:
            return i
    return -1

name_list = ['nahid', 'hassan', 'mony', 'mahin', 'meem', 'bristy']
idx = linear_search(name_list, 'meem')
print(idx, name_list[idx])