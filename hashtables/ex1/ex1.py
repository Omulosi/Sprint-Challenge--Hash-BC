#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    # store weight-index pairs in the ht
    for index, weight in enumerate(weights):
        difference = limit - weight
        if hash_table_retrieve(ht, difference) is not None:
            if hash_table_retrieve(ht, difference) > index:
                return [hash_table_retrieve(ht, difference), index]
            return [i, hash_table_retrieve(ht, difference)]
        else:
            hash_table_insert(ht, weight, index)

    # search for indices with weigths that add up to limit
    max_indices = ()



    return ht


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
