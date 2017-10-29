# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:35:34 2017

@author: hzwangxinzhe1
"""

import numpy as np
import math

def load_dataset(filename):
    attr = np.loadtxt(filename, delimiter = '\t', dtype = 'S10', usecols = (0, 1, 2, 3))
    labels = np.loadtxt(filename, delimiter = '\t', usecols = 4, dtype = 'S1')
    return attr, labels


def cal_shannon_ent(dataset):
    # calculate total number
    instance_num = len(dataset)
    # get every class's number
    class_map = {}
    for ins in dataset:
        k = ins[-1]
        if class_map.has_key(k):
            class_map[k] += 1
        else:
            class_map[k] = 1
    shannon_ent = 0.0
    for val in class_map.itervalues():
        prob = float(val) / instance_num
        shannon_ent += prob * math.log(prob, 2)
    return shannon_ent
                                                                 