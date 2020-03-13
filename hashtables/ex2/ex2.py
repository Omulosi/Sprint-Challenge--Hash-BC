from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    # Add tickets to hash table
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    # Start from initial source
    current = hash_table_retrieve(hashtable, "NONE")

    for i in range(length - 1):
        route[i] = current
        current = hash_table_retrieve(hashtable, current)

    return list(filter(None, route))
