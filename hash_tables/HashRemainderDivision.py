from hash_tables.HashTable import HashTable


class HashRemainderDivision(HashTable):

    def hash_key(self, key, radix=10, decode='utf-8'):
        key = list(bytes(key, decode))

        buff = 0
        for i in range(len(key) - 1, -1, -1):
            buff += key[i] * radix ** i
            pass

        key = buff
        return key % self.size
