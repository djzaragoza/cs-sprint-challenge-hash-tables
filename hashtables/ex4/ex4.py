def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create open dict
    my_dict = {}

    # create open list
    pos_nums = []

    # for all of the numbers in a
    for num in a:
        # add all of the numbers to my dictionary
        my_dict[num] = 1

        if num * -1 in my_dict and num != 0:
            pos_nums.append(abs(num))

    return pos_nums


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
