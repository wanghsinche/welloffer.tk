# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 17:34:24 2017

@author: hzwangxinzhe1
"""
import numpy as np
import math 
def create_vacabulary_list(dataset):
    v_set = set([])
    for row in dataset:
        v_set.update(row)
    return list(v_set)


def loadDataSet():
    """
    测试数据，每行可看成一个文章包含的词
    返回文章列表及其分类向量
    """
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 不和谐, 0 正常
    return postingList,classVec
def createVocabList(dataSet):
    """
    返回词汇列表
    ['cute', 'love', 'help', 'garbage', 'quit', 'I',...
    """
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document) # 求并集
    return list(vocabSet)
def setOfWords2Vec(vocabList, inputSet):
    """
    返回一个向量，表示文档中的词汇是否出现在词汇表中，其实这里并没有反映字频信息，比如bitch出现了多次的文章，肯定比出现一次的文章要更加偏向于不和谐的文章，后面会有阐述
    [0, 1, 0...
    """
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: print "the word: %s is not in my Vocabulary!" % word
    return returnVec


def trainNB0(trainMatrix,trainCategory):
    """
    :param trainMatrix:
    [
        [1,0,...],
        [0,1,...]
    ]
    :param trainCategory:
    [1,0,...]
    :return:
    """
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    # 不和谐文档的概率
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    # 每个词出现的次数初始化为1，防止后面计算p(x1|c)p(x2|c)...p(xn|c)的时候为0
    p0Num = np.ones(numWords); p1Num = np.ones(numWords)
    p0Denom = 2.0; p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            # 向量和，统计类比1下每个词的总数
            p1Num += trainMatrix[i]
            # 得到类别1下的总次数
            p1Denom += np.sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += np.sum(trainMatrix[i])
    print p1Denom, p0Denom
    print np.sum(p1Num-np.ones(numWords)), np.sum(p0Num-np.ones(numWords))
    # 避免p(x1|c)p(x2|c)...p(xn|c)得到很小的数最后四舍五入为0
    p1Vect = np.log(p1Num/p1Denom)
    p0Vect = np.log(p0Num/p0Denom)
    # 返回p(w|0) p(w|1) p(1) 这里w是向量
    return p0Vect,p1Vect,pAbusive

