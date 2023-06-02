from Contact import Contact


class HashTable:
    def __init__(self, size):
        self._size = size
        self._table = [None] * size


    def _hash_function(self, key):
        key = 0
        for i, x in enumerate(repr(key)):
            key += ord(x) + i
        return key % self.size()

    def _rehash(self, old_key):
        return old_key+1 % self.size()

    def size(self):
        return len(self._table)

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
            for k, v in self._table[index]:
                if k == key:
                    return True
        return None

    def delete(self, key):
        print()

    def __str__(self):
        out = '{'
        for i in range(self.size()):
            for item in self._table[i]:
                out += f' {item[0]}: {item[1][0]}, {item[1][1]} | '
        return out[:-2] + '}'

