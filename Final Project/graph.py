#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 13:35:33 2018

@author: yx4247
"""

import random
from collections import deque

class graph:
    def __init__(self):
        self.count = dict()
        self.map = dict()
        self.size = 0
        self.origin = dict()
        
    def addElem(self, dq, token = None):
        word = ' '.join(dq)
        if word not in self.map:
            self.map[word] = dq.copy()
        if word not in self.count:
            self.count[word] = Node()
        self.count[word].addToken(token)
        self.size += 1
    
    def train(self, data, level):
        dq = deque()
        for token in data:
            self.origin[str(token)] = token
            token = str(token)
            if len(dq) == level:
                self.addElem(dq, token)
                dq.popleft()
            dq.append(token)
            
    def newState(self):
        num = random.randint(1, self.size)
        for key, value in self.count.items():
            num -= value.size
            if num <= 0:
                return self.map[key].copy()
    
    def check(self, word):
        return word not in self.count
    
    def original(self, token):
        return self.origin[token]

class Node:
    def __init__(self):
        self.prob = dict()
        self.size = 0
    
    def addToken(self, token = None):
        self.size += 1
        if token not in self.prob:
            self.prob[token] = 1
        else:
            self.prob[token] += 1
            
    def getToken(self):
        num = random.randint(1, self.size)
        for key, value in self.prob.items():
            num -= value
            if num <= 0:
                return key
            