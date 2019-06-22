


import numpy as np
import math
import scipy.special as scipy
from meshgrid import  meshgrid
def makeVonMisses(R0,theta0,dim1,dim2):


    msk1 = np.zeros((len(dim1),len(dim2)))
    msk2 = msk1
    sigma_r = R0/2
    B = R0
    if( dim2[0] == min(dim2)):
        dim2 = np.flip(dim2,axis=0)

    X,Y = meshgrid(dim1,dim2)

    R = np.sqrt(X**2+Y**2)
    theta = np.arctan2(Y,X)

    msk1 = np.exp(B * np.cos(theta-(theta0)))/scipy.jv(0,R-R0)
    msk1 = msk1/np.max(msk1)
    msk2 = np.exp(B * np.cos(theta - (theta0+math.pi))) / scipy.jv(0, R - R0)
    msk2 = msk2 / np.max(msk2)

    return msk1,msk2