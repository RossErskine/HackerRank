#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dot and Cross

Created on Thu Dec  1 21:06:30 2022

@author: roscopikotrain
"""

import numpy as np

N = int(input("Enter N?"))
A =np.zeros((N, N))

for _ in range(N):
    a1 = int(input())
    a2 = int(input())
    A = np.array([[a1],[a2]])
    

    