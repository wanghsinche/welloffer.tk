# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:35:34 2017

@author: hzwangxinzhe1
"""

import numpy as np


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
        if class_map
    
                                                                 