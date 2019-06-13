import sys
import pandas as pd
import math
import os

def load_file(file):
    dataset = pd.read_csv(file)
    return dataset

def entropy(target):
    ent = 0
    result = {}
    target_n = len(target)
    for target_data in target:
        if target_data in result:
            result[target_data] += 1
        else:
            result[target_data] = 1
    for label in result.keys():
        p_x = result[label] / target_n
        ent += - p_x * math.log(p_x,2)
    return ent

def avg_entropy_partitions(partition_data):
    avg_entropy = 0
    total = 0
    for partition in partition_data.values():
        avg_entropy += entropy(partition) * len(partition)
        total += len(partition)
    avg_entropy /= total
    return avg_entropy

def partition(data, attribute, target):
    partition_data = {}
    target_data = {}
    indx = 0
    for element in data[attribute]:
        if element in partition_data:
            for attr in data.keys():
                partition_data[element][attr].append(data[attr][indx])
        else:
            partition_data[element] = {}
            for attr in data.keys():
                partition_data[element][attr] = list()
                partition_data[element][attr].append(data[attr][indx])
            target_data[element] = list()
        target_data[element].append(target[indx])
        indx += 1
    return partition_data, target_data

def common_target(target_data):
    most_frequent = 0
    target = target_data[0]
    for data in target_data:
        count_data = target_data.count(data)
        if count_data > most_frequent:
            most_frequent = count_data
            target = data
    return target

def id3(data, target):
    node = {}
    if len(data) == 0:
        return {'result': common_target(target)}
    max_winnings = None
    max_attribute = None
    max_attribute_data = None
    max_target_data = None
    general_entropy = entropy(target)
    if general_entropy == 0:
        return {'result': common_target(target)}
    for attribute in data:
        attribute_data, target_data = partition(data, attribute, target)
        avg_entropy = avg_entropy_partitions(target_data)
        winning = general_entropy - avg_entropy
        if max_winnings is None or winning > max_winnings:
            max_winnings = winning
            max_attribute = attribute
            max_attribute_data = attribute_data
            max_target_data = target_data
    node[max_attribute] = {}
    for attr_data in max_attribute_data:
        del max_attribute_data[attr_data][max_attribute]
        node[max_attribute][attr_data] = id3(max_attribute_data[attr_data], max_target_data[attr_data])
    return node

def main():
    argv = sys.argv
    dataset = load_file(argv[1])
    target = dataset[dataset.keys()[-1]]
    del dataset[dataset.keys()[-1]]
    node = id3(dataset,target)

if __name__ == "__main__":
    main()
