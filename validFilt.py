# import tensorflow as tf
# import  numpy as np
import scipy.ndimage
def validFilt(map,msk):
    newMap = scipy.ndimage.convolve(map,msk, mode='nearest')

    return newMap
