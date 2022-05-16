from chapter07.p12 import HashTable


def test_hashtable():
    values = ["sheep", "dog", "deer", "cat", "whale", "roaster", "mice", "octopus", "cow"]
    hashtable = HashTable(10)
    for v in values:
        hashtable[v] = v

    for v in values:
        assert hashtable[v] == v

    del hashtable["sheep"]
    print(hashtable)
