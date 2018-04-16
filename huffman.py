#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:53:39 2018

@author: pritish
"""

import cv2
import numpy as np
from scipy.stats import itemfreq


def coding(A):
    A.sort()
    
    if len(A)==2:
        return ['1','0']
    
    A=A[::-1]
    temp=A[:-2]
    for i in range(len(temp)):
        if temp[i]<A[len(A)-1]+A[len(A)-2]:
            break
    
    temp.append(A[len(A)-1]+A[len(A)-2])
    t1=coding(temp) 
    A=A[::-1]
    if A[len(A)-1]>A[len(A)-2]:
        a=t1[i]+'0'
        b=t1[i]+'1'
        t1.append(a)
        t1.append(b)
        t1.remove(t1[i])
    else:
        a=t1[i]+'1'
        b=t1[i]+'0'
        t1.append(a)
        t1.append(b)
        t1.remove(t1[i])
        
    return t1
            
        
    
img=cv2.imread('/home/pritish/digicommassn/data1.bmp',1)
img=img[:,:,0]


out=np.copy(img).astype(str)

freqtable=itemfreq(img)

sortfreq=np.copy(freqtable[:,1])
sortfreq.sort()
uniqfreq=np.unique(sortfreq)
sortfreq=sortfreq/np.sum(sortfreq)
sortfreq=list(sortfreq)

temp=[]
for i in uniqfreq:
    for j in range(freqtable.shape[0]):
        if freqtable[j][1]==i:
            temp.append(freqtable[j][0])


code=coding(sortfreq)
code=code[::-1]

dic={}

for i in range(len(temp)):
    dic[temp[i]]=code[i]


outstr=0

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        outstr+=len(dic[img[i][j]])

out=540*1024*8
    

A=[42,7,4,2,2,2,2,1,1,1]

c=coding(A)





    
    

    
    
        

