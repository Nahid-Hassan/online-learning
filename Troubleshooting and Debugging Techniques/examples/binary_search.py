def binary_search(list, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    left = 0
    right = len(list) - 1
    
    while left <= right:
        middle = (left + right) // 2

        if list[middle] == key:
            return middle
        if list[middle] > key:
            right = middle - 1
        if list[middle] < key:
            left = middle + 1
    return -1

name_list = ['nahid', 'hassan', 'mony', 'mahin', 'meem', 'bristy']
name_list.sort()
print(name_list)
idx = binary_search(name_list, 'meem')
print(idx, name_list[idx])
