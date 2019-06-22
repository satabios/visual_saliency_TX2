#-------------------------------------------------------------------------------
# Name:        main
# Purpose:     Testing the package pySaliencyMap
#
# Author:      Akisato Kimura <akisato@ieee.org>
#
# Created:     May 4, 2014
# Copyright:   (c) Akisato Kimura 2014-
# Licence:     All rights reserved
#-------------------------------------------------------------------------------

import cv2
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
#matplotlib.use('Agg')
 

import pySaliencyMap
import time
import numpy as np
import matplotlib.pyplot as plt
from generateChannels import  generateChannels
from makeBorderOwnership import makeBorderOwnership
# from salienpy.salienpy.commons import minmaxnormalization
# from ittiNorm import ittiNorm
# from numba import vectorize, cuda
#from multiprocessing import Process
import threading
global imgs
from makeDefaultParams import makeDefaultParams
from computeTemporalFiltering import computeTemporalFiltering
#from normalizeImage import  normalizeImage

import h5py
from ComputeTemporalFilter_jam import ComputeTemporalFilter_jam
import tensorflow as tf
from makeTemporalFilter import makeTemporalFilter
tf.enable_eager_execution()
import cv2
import matplotlib.pyplot as plt


def normalizeImage(num,frame):

    if(len(frame)<=1):
        rn =[0,1]
    else:
        rn = frame[1]

    mx = tf.reduce_max(frame[0])
    mn = tf.reduce_min(frame[0])
    frame = tf.divide(tf.subtract(frame[0], mn), tf.subtract(mx, mn)) * abs(rn[1]-rn[0]) + min(rn)


    imgs[:,:,:,num] = frame



if __name__ == '__main__':


    # with h5py.File('./video_explosion.mat', 'r') as f:
         # video = tf.constant(np.transpose(f['video'],[1,0,3,2]))

    params = makeDefaultParams(1e5)
    cap = cv2.VideoCapture(1)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)
    width  = 640
    height = 480
    #
    
    
    #cap= cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)308, height=(int)308,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    sm = pySaliencyMap.pySaliencyMap(height,width)
    
    r_s = np.reshape(makeTemporalFilter('strong_t3'), (3,1,1,1))
    r_w = np.reshape(makeTemporalFilter('weak_t6'), (6,1,1,1))
    imgs = np.zeros((height,width,3,3))
    print(r_s.shape)
   
    video = np.zeros((6,height,width,3))
    for i in range(6):
            ret, frame = cap.read()
            print(np.asarray(frame).shape)
            video[i,:,:,:]= frame
    imgs = np.zeros((video[0].shape[0], video[0].shape[1], video[0].shape[2], len(params['channels'])))

    while (True):
        
        
        st = time.time()
        video[:5,:,:,:] = video[1:,:,:,:]
        ret, frame = cap.read()
        video[5,:,:,:]= frame
        #video = np.asarray(video)
      
        temp_out_strong, temp_out_weak = ComputeTemporalFilter_jam(video,r_s,r_w)
        print(len(temp_out_strong))
        print(temp_out_weak.shape)
        print(video[2].shape)
        p1 = threading.Thread(target=normalizeImage,args=(0,temp_out_strong))
        p2 = threading.Thread(target=normalizeImage,args=(1,temp_out_weak))
        p3 = threading.Thread(target=normalizeImage,args=(2,video[2]))

        p1.start()
        p2.start()
        p3.start()
        
        p1.join()
        p2.join()
        p3.join()
        
        R, G, B, inp = generateChannels(imgs, params)

        salmap = sm.sal_map(R, G, B,inp)
    
        cv2.imshow('Video', salmap)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        print("FPS:",1/(time.time()-st))
        #if cv2.waitKey(1) == 27: 
        #    break  # esc to quit
        
    
        #print("map_time:",time.time()-st,"\n")
    cv2.destroyAllWindows()
    

        # img = tf.add(imgs,axis=)
