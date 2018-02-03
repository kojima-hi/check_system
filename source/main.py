#!/bin/usr/env python
# -*- coding: utf-8 -*-
from IO import get_parse, get_structure
from check import check_oberlap

def main():
    args = get_parse()

    structure = get_structure(args.input)

    if args.type == 'overlap':
        check_oberlap(structure, thresh_A=args.threshold, exclude=args.exclude)

    return


if __name__ == "__main__":
    main()
