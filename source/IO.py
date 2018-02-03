#!/bin/usr/env python
# -*- coding: utf-8 -*-
import argparse
import os
import numpy as np


def get_parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('-i', '--input', type=str, required=True,
                        help='input GRO file (INPUT)')
    parser.add_argument('-t', '--type', type=str, required=True,
                        choices=['overlap'],
                        help='check type (INPUT)')
    parser.add_argument('-th', '--threshold', type=float, default=1.0,
                        help='threshold (INPUT, option)')
    parser.add_argument('-e', '--exclude', type=int, default=0,
                        help='number of exclusion (INPUT, option)')


    return parser.parse_args()


def __get_structure_gro(path):
    structure = {}

    with open(path, 'r') as f:
        _ = f.readline() # read comment line
        num_atom = int(f.readline())

        position = np.zeros((num_atom, 3), dtype=np.float32)
        for i in range(num_atom):
            pos_str = (f.readline())[20:44]
            position[i, :] = np.array(pos_str.split(), dtype=np.float32)

        items = (f.readline().strip()).split()
        system_size = np.array(items, dtype=np.float32)

    structure['pos'] = position
    structure['sys_size'] = system_size
    return structure


def get_structure(path):

    ext = (os.path.splitext(path))[1]
    if ext == '.gro':
        structure = __get_structure_gro(path)

    return structure


def main():
    return


if __name__ == "__main__":
    main()
