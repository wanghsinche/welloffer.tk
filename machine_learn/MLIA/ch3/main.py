# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:36:16 2017

@author: hzwangxinzhe1
"""

import tree
import numpy as np

def main():
#    print tree.load_dataset('lenses.txt')
    dataset = np.array([
            [1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'],
            [0, 1, 'no'], [0, 1, 'no']
            ])
    print tree.cal_shannon_ent(dataset)
    print tree.cal_con_shannon_ent(dataset, 1)

if __name__ == '__main__':
    main()