from functools import lru_cache


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        connections = dict( reversed(i.split(')')) for i in f.read().splitlines() )

    @lru_cache(32)
    def recursive(node):
        return recursive(connections[node]) + 1 if node in connections else 0

    def find_parent(node):
        return find_parent(connections[node]) | {connections[node]} if node in connections else set()

    no_of_connections = 0
    for connection in connections:
        no_of_connections += recursive(connection)


    print(no_of_connections)
    # print(find_parent('YOU'))
    # print(find_parent('SAN'))
    print(len (find_parent('YOU') | find_parent('SAN')) - len(find_parent('YOU') & find_parent('SAN')))