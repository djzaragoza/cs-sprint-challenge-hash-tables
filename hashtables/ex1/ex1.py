def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # create an open dict

    hash_table = {}

    # will loop if there's a key present, get() the limit minus the weights at i-th index
    for i in range(length):
        results = hash_table.get(limit - weights[i])

        if results != None:
            return i, results

        # set hash_table at the weights at the i-th index ... index equal it i
        hash_table[weights[i]] = i

    return None
