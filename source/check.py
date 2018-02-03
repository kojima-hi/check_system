#!/bin/usr/env python
# -*- coding: utf-8 -*-
import numpy as np


def check_oberlap(structure, thresh_A=1.0, exclude=0):
    position = structure['pos']
    system_size = structure['sys_size']
    system_size_h = system_size / 2.0
    n_atom = position.shape[0]

    thresh_nm = thresh_A * 0.1
    for i in range(n_atom - 1):
        pos_i = position[i]
        for j in range(i + 1 + exclude, n_atom):
            pos_j = position[j]

            dpos = pos_i - pos_j
            for k in range(3):
                over_bc = True
                while over_bc:
                    if dpos[k] < -system_size_h[k]:
                        dpos[k] += system_size[k]
                    elif dpos[k] >= system_size_h[k]:
                        dpos[k] -= system_size[k]
                    else:
                        over_bc = False

            dl = np.linalg.norm(dpos)

            if dl < thresh_nm:
                print('Overlap: %i %i %f (nm)'%(i, j, dl))


    return


def main():
    return


if __name__ == "__main__":
    main()