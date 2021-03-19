from hash_tables.HashTable import HashTable


class HashXOR(HashTable):

    def hash_key(self, key):
        hashed_key = 0
        for i in range(len(key)):
            hashed_key ^= ord(key[i])

        return hashed_key
