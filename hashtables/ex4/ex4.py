import math


def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create hash table
    hash_table = {}
    result = []

    # for all of the numbers in a
    for num in a:
        # add all of the numbers to hash table
        abs_val = abs(num)

        if hash_table.get(abs_val) is not None:
            result.append(abs_val)
        else:
            hash_table[abs_val] = abs_val

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
