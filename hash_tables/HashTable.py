from abc import abstractmethod


class HashTable:

    def __init__(self, size=1000):
        self.table = []
        self.size = size
        for i in range(size):
            self.table.append(None)
            pass
        pass

    @abstractmethod
    def hash_key(self, key):
        pass

    def linear_probe(self, key, i):
        return (self.hash_key(key) + i) % self.size

    def find(self, key):
        for i in range(self.size):
            if self.table[self.linear_probe(key, i)] == key:
                return self.linear_probe(key, i)

        return None
        pass

    def insert(self, key):
        for i in range(self.size):
            if not self.table[self.linear_probe(key, i)]:
                self.table[self.linear_probe(key, i)] = key
                return self.linear_probe(key, i)
            pass

        raise OverflowError('Table is full already')
        pass

    def delete(self, key):
        for i in range(self.size):
            if self.table[self.linear_probe(key, i)] == key:
                self.table[self.linear_probe(key, i)] = None
                return self.linear_probe(key, i)

        raise OverflowError('Table has no items already')
        pass
