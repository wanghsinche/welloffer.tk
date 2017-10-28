# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

def create_data_set():
    group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A','A','B','B']
    return group, labels


def classify0(in_x, dataset, labels, k):
    dataset_size = dataset.shape[0];
    diffmat = np.tile(in_x, (dataset_size, 1)) - dataset
    sq_diffmat = np.power(diffmat, 2)
    sq_distances = sq_diffmat.sum(axis = 1)
    distances = np.power(sq_distances, 0.5)
    sorted_dist_indicies = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_label = labels[sorted_dist_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1
    return max(class_count.iterkeys(), key = (lambda k: class_count[k]))


def load_testset_manul(filename):
    fr = open(filename)
    rows = fr.readlines()
    testmat = np.zeros((len(rows), 3))
    for index, line in enumerate(rows):
        tok = line.split('\t')
        testmat[index, :] = tok[0:3]
    return testmat


def load_testset(filename):
    arr = np.loadtxt(filename, delimiter = '\t', usecols = (0, 1, 2))
    label = np.loadtxt(filename, delimiter = '\t', dtype = 'S1', usecols = 3)
    return arr, label


def norm(mat):
    range_mat = mat.max(axis = 0) - mat.min(axis = 0)
    val_mat = mat - mat.min(axis = 0)
    return val_mat / range_mat, range_mat, mat.min(axis = 0)