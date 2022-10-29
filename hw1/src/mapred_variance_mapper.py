#!/usr/bin/env python3

import csv
import sys

COLUMN_NAME = 'price'
COLUMN_IDX = 9


def read_csv_column_values():
    for row in csv.reader(sys.stdin):
        value = row[COLUMN_IDX]
        if value is not None and value != COLUMN_NAME:
            yield float(value)


def mapper_variance():
    chunk_first_momentum = 0.
    chunk_second_momentum = 0.
    chunk_size = 0

    for value in read_csv_column_values():
        chunk_first_momentum += value
        chunk_second_momentum += value * value
        chunk_size += 1

    if chunk_size > 0:
        chunk_mean = chunk_first_momentum / chunk_size
        chunk_variance = chunk_second_momentum / chunk_size - (chunk_mean ** 2)
        print('{}\t{}\t{}'.format(chunk_mean, chunk_variance, chunk_size))


if __name__ == '__main__':
    mapper_variance()
