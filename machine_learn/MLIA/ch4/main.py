# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:25:12 2017

@author: hzwangxinzhe1
"""

import bayes
import numpy as np

def main():
    postingList,classVec = bayes.loadDataSet()
    vlist= bayes.create_vacabulary_list(postingList)
    tranmat = []
    for row in postingList:
        tranmat.append(bayes.setOfWords2Vec(vlist,row))
    print bayes.trainNB0(tranmat, classVec)
    


if __name__ == '__main__':
    main()