import pandas as pd
import time


def check_hashing_time(hash_table, data, mode, shift=0):
    times = []

    counter = 0
    if mode == 'find':
        for i in data[shift:]:
            timer = time.process_time()

            hash_table.find(i)

            times.append(time.process_time() - timer)

            counter += 1
            if counter == hash_table.size:
                break
            pass
        pass
    elif mode == 'insert':
        for i in data[shift:]:

            timer = time.process_time()

            hash_table.insert(i)

            times.append(time.process_time() - timer)

            counter += 1
            if counter == hash_table.size:
                break
            pass
        pass
    elif mode == 'delete':
        for i in data[shift:]:

            timer = time.process_time()

            hash_table.delete(i)

            times.append(time.process_time() - timer)

            counter += 1
            if counter == hash_table.size:
                break
            pass
        pass
    return times


def research_time(hashers_dict, testing_data, shift=0):
    df = pd.DataFrame()

    hasher_names = ['Remainder_Division', 'XOR']
    modes = ['insert', 'find', 'delete']

    for mode in modes:
        for hasher_name in hasher_names:
            df[hasher_name + '_' + mode] = pd.Series(
                check_hashing_time(hashers_dict.get(hasher_name), testing_data,
                                   mode, shift))
            pass
        pass
    return df
