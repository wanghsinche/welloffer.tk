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
                                                                 

def cal_con_shannon_ent(dataset, col):
    # split dataset
    # by column value
    val_class_map = {}
    total_row = float(len(dataset))
    for val in dataset:
        k = val[col]
        if val_class_map.has_key(k):
            val_class_map[k].append(val)
        else:
            val_class_map[k] = [val]
    # to np array
    for row in val_class_map.iterkeys():
        val_class_map[row] = np.array(val_class_map[row])
    # calculate entropy
    con_shannon_ent = 0.0
    for val_class_row in val_class_map.itervalues():
        di_d = len(val_class_row) / total_row
        con_shannon_ent += di_d * cal_shannon_ent(val_class_row)
    return con_shannon_ent, val_class_map
    
    
    
    