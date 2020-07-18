def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here

    # get count of array
    arr_count = len(arrays)

    # create open dict
    total = {}

    # need to find total for the first list, at 0th position
    for i in arrays[0]:
        # add all i to the total dict
        total[i] = 1

    # for every list after
    for next_arr in arrays[1:]:
        # find total occurences
        for new_item in next_arr:
            # if new item is in total dict
            if new_item in total:
                # increment total at new_item-th index by 1
                total[new_item] += 1

        # iterate through key and value in total dict and set equal to result
        result = [key for (key, val) in total.items() if val == arr_count]
    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
