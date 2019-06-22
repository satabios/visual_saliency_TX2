

import  math
import numpy as np
from makeVonMisses import makeVonMisses
from validFilt import validFilt
import scipy.ndimage
def vonMisesPyramid(map,vmPrs):

    data = [map,map,map,map]
    msk = np.zeros((10,13,13))
    ori  = np.zeros((4,10))

    msk1 = {'data':msk,'ori':ori}
    msk2 = msk1
    pyr1 = {'data':data,'ori':ori}
    pyr2 = pyr1



    for ori in range(vmPrs['numOri']):
        dim1 = np.asarray(range(-3 * vmPrs['R0'], 3 * vmPrs['R0'] + 1))
        dim2 = dim1
        msk_1, msk_2 = makeVonMisses(int(vmPrs['R0']), vmPrs['oris'][ori] + math.pi / 2, dim1, dim2)
        msk1['data'][ori] = msk_2
        msk2['data'][ori] = msk_1

        for l in range(vmPrs['maxLevel']):

            pyr1['data'][ori][l] = scipy.ndimage.correlate(map[l],msk_1, mode='constant')#validFilt()  #check for convolution type; used scipy valiFilt function
            pyr2['data'][ori][l] = scipy.ndimage.correlate(map[l], msk_2, mode='constant')

            msk1['ori'][ori][l] = vmPrs['oris'][ori]+math.pi/2
            msk2['ori'][ori][l] = vmPrs['oris'][ori] + math.pi / 2
            pyr1['ori'][ori][l] = vmPrs['oris'][ori] + math.pi / 2
            pyr2['ori'][ori][l] = vmPrs['oris'][ori] + math.pi / 2


    return pyr1,msk1,pyr2,msk2