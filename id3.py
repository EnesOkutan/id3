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

def main():
    argv = sys.argv
    dataset = load_file(argv[1])
    target = dataset[dataset.keys()[-1]]
    del dataset[dataset.keys()[-1]]

if __name__ == "__main__":
    main()
