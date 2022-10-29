#!/usr/bin/env python3

import argparse
import pandas as pd


def parse_args():
    parser = argparse.ArgumentParser(
        description='Calculates mean and variance for chosen csv file column'
    )
    parser.add_argument('csv_file', help='path to csv file')
    parser.add_argument('column', help='column name')
    return parser.parse_args()


def main():
    args = parse_args()
    column = pd.read_csv(args.csv_file, usecols=[args.column])[args.column]
    print('mean', column.mean())
    print('variance', column.var())


if __name__ == '__main__':
    main()
