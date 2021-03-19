def read_data_txt(path, encoding='utf-8'):
    testing_data = 0

    with open(path, 'r', encoding=encoding) as f:
        testing_data = f.readlines()[0].split()
        pass
    f.close()

    return testing_data


def hash_data(hash_table, data, shift=0):
    counter = 0
    for i in data[shift:]:

        hash_table.insert(i)

        counter += 1
        if counter == hash_table.size:
            break
        pass
    return hash_table
