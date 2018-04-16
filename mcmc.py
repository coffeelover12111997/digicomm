#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 21:17:09 2018

@author: pritish
"""

#MonteCarloMarkovChain(using metropolis algorithm)

#4x4 lattice(assuming a std normal prior distn)

import numpy as np
from scipy.stats import itemfreq
import scipy
from scipy.stats import norm
import matplotlib.pyplot as plt




def prior(x):
    return norm.pdf(x)# assuming a normal prior

def mcmc(data,iteration):
    freq=list(data)
    presentstate=data.pop()
    for i in range(iteration):
        temp=itemfreq(np.array(freq))
        dic=dict(zip(temp[:,0],temp[:,1]))
        priorarray=prior(np.array(data)-presentstate)
        index=scipy.argmax(priorarray)
        nxtstate=data[index]
        acceptance=min((1,dic[nxtstate]/dic[presentstate]))#since we assumed symmetric prior
        cointoss=np.random.random_sample()
        if acceptance>=cointoss:
            data.append(presentstate)
            presentstate=nxtstate
            freq.append(nxtstate)
            data.remove(nxtstate)
        else:
            freq.append(presentstate)
    return freq
            
def main():
    data=[0,0.1,0.2,0.3]
    plt.hist(data)
    #specify i for no of iterations
    for i in [600,700,800,900,1000]:
        out=mcmc(data,i)
        plt.hist(out)
        data=[0,0.1,0.2,0.3]
    
    




if __name__=='__main__':
    main()
            
                
                
            
        



    
    
    
    
        