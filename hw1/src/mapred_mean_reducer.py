#!/usr/bin/env python3

import csv
import sys


COLUMN_NAME = 'price'
COLUMN_IDX = 9


def read_mapper_outputs():
    for chunk_mean, chunk_size, in csv.reader(sys.stdin, delimiter='\t'):
        yield float(chunk_mean), int(chunk_size)


def weighted_mean(weight1, mean1, weight2, mean2):
    return (weight1 * mean1 + weight2 * mean2) / (weight1 + weight2)


def reducer_mean():
    total_mean = 0.
    total_size = 0
    for chunk_mean, chunk_size in read_mapper_outputs():
        total_mean = weighted_mean(total_size, total_mean, chunk_size, chunk_mean)
        total_size += chunk_size

    print('mean', total_mean)


if __name__ == '__main__':
    reducer_mean()
