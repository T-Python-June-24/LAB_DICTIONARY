given_list = [5, 0, 34, 9, 0, 13, 8]

def zero_at_end(list1):
    result = [] #list for non-zero elts
    zero_count = 0  # counter to move onto next elt

    for num in list1:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    result.extend([0] * zero_count)
    return result


result = zero_at_end(given_list)
print(result)