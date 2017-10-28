# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 10:32:14 2017

@author: hzwangxinzhe1
"""

import knn
import numpy as np
import matplotlib.pyplot as plt


def label2color(v):
    if v == 'd':
        return 'b'
    elif v == 's':
        return 'g'
    elif v == 'l':
        return 'r'
    else:
        return 'c'
    

def main():
#    group, labels = knn.create_data_set()
#    print knn.classify0([0, 0], group, labels, 3)
     arr, labels = knn.load_testset('./datingTestSet.txt')
#     arr, range_mat, min_mat =  knn.norm(arr)
#     in_x = np.array([40920, 8.326976, 0.953952])
#     norm_in_x = (in_x - min_mat) / range_mat
#     print knn.classify0(norm_in_x, arr, labels, 10)
     fig = plt.figure()
     ax = fig.add_subplot(111)
     vfunc = np.vectorize(label2color)
     ax.scatter(arr[:, 0], arr[:, 1], c = vfunc(labels))
     plt.show()
    

    
if __name__ == '__main__':
    main()