from Contact import Contact


class HashTable:
    def __init__(self, size):
        self._size = size
        self._table = [None] * size

    def _hash_function(self, key):
        new_key = 0
        for i, x in enumerate(repr(key)):
            new_key += ord(x) + i
        return new_key % self._size

    def _rehash(self, old_key):
        return old_key + 1 % self._size

    def size(self):
        count = 0
        for slot in self._table:
            if slot is not None:
                count += len(slot)
        return count

    def put(self, key, value):
        index = self._hash_function(key)
        if self._table[index] is None:
            self._table[index] = [(key, value)]
        else:
            index = self._rehash(index)
            self._table[index] = [(key, value)]

    def get(self, key):
        index = self._hash_function(key)
        if self._table[index] is not None:
            for item in self._table[index]:
                # print(item[0])
                if item[0] == key:
                    return item[0]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        print(index)
        if self._table[index] is not None:
            for i, item in enumerate(self._table[index]):
                print(item[0],key)
                if item[0] == key:
                    del self._table[index][i]
                    return True

    def __str__(self):
        out = '{'
        for i in range(self._size):
            if self._table[i] is not None:
                for item in self._table[i]:
                    out += f' {item[0]}: {item[1][0]}, {item[1][1]} | '
        out += '}'
        return out
