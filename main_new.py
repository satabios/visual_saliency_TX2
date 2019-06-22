# -------------------------------------------------------------------------------
# Name:        main
# Purpose:     Testing the package pySaliencyMap
#
# Author:      Akisato Kimura <akisato@ieee.org>
#
# Created:     May 4, 2014
# Copyright:   (c) Akisato Kimura 2014-
# Licence:     All rights reserved
# -------------------------------------------------------------------------------

import cv2
import matplotlib.pyplot as plt
import matplotlib
# matplotlib.use('TkAgg')
# matplotlib.use('Agg')


import pySaliencyMap
import time
import numpy as np
from generateChannels import generateChannels
from makeBorderOwnership import makeBorderOwnership
# from salienpy.salienpy.commons import minmaxnormalization
# from ittiNorm import ittiNorm
# from numba import vectorize, cuda
from multiprocessing import Process
from makeColors import makeColors

from makeDefaultParams import makeDefaultParams
from computeTemporalFiltering import computeTemporalFiltering
#from normalizeImage import normalizeImage
# main
# @vectorize(['float32(float32)'],target='cuda')
# def static(img):
#     # read
#     # img = cv2.imread('test3.jpg')
#     # initialize
#     img = np.transpose(img,[1,2,0])
#     imgsize = img.shape
#     img_width  = imgsize[1]
#     img_height = imgsize[0]
#     sm = pySaliencyMap.pySaliencyMap(img_width, img_height)
#     sm = sm.SMGetSM(img)
#     # computation
#     # start = time.time()
#     # for i in range(100):
#     # sal_map = []
#     # for i in range(3):
#     # sal_map.append()
#
#
#
#     return sm

import h5py
from ComputeTemporalFilter_jam import ComputeTemporalFilter_jam
import tensorflow as tf
from makeTemporalFilter import makeTemporalFilter
from normalizeImage_new import normalizeImage
#tf.enable_eager_execution()
import cv2
import matplotlib.pyplot as plt

if __name__ == '__main__':

  

    params = makeDefaultParams(1e5)
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    

    # cap= cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)308, height=(int)308,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    sm = pySaliencyMap.pySaliencyMap(height, width)

    r_s = np.reshape(makeTemporalFilter('strong_t3'), (3, 1, 1, 1))
    r_w = np.reshape(makeTemporalFilter('weak_t6'), (6, 1, 1, 1))
    imgs = np.zeros((height, width, 3, 3))
    #print(r_s.shape)
   
    video = np.zeros((6, height, width, 3))
    start = time.time()
    for i in range(6):
        ret, frame = cap.read()
        #print(np.asarray(frame).shape)
        video[i, :, :, :] = frame
    imgs = np.zeros((video[0].shape[0], video[0].shape[1], video[0].shape[2], len(params['channels'])))
    # plt.ion()
    salmap = np.zeros((height, width))
    # plt.title("Histogram")
    # cv2.namedWindow('frame')
    while (True):
       
        start = time.time()
        video = np.roll(video, -1, axis=0)
        
        ret, frame = cap.read()
        video[5, :, :, :] = frame

        

      
        temp_out_strong, temp_out_weak = ComputeTemporalFilter_jam(video, r_s, r_w)
        
        #print("shape:",imgs[:, :, :, 0].shape)
        imgs[:, :, :, 0] = normalizeImage(temp_out_strong)
        imgs[:, :, :, 1] = normalizeImage(temp_out_weak)
        imgs[:, :, :, 2] = normalizeImage(video[2])
       
        [inp, in_orient, R, G, B, Y] = makeColors(imgs)
        
        salmap = sm.sal_map(R, G, B, inp)
        
        cv2.imshow('orig',frame)
        cv2.imshow('frame', cv2.applyColorMap((((-1 * cv2.resize(salmap, (0,0), fx=3, fy=3)) / 32) * 255).astype(np.uint8), cv2.COLORMAP_JET))
        #print("time", 6*1 / (time.time() - start))
        

        
        if cv2.waitKey(1) == 27:
            break  

       
    cv2.destroyAllWindows()
  
