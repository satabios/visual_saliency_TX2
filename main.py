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
#import matplotlib.pyplot as plt
import pySaliencyMap
import time
import numpy as np
from generateChannels import  generateChannels
from makeBorderOwnership import makeBorderOwnership
# from salienpy.salienpy.commons import minmaxnormalization
# from ittiNorm import ittiNorm
# from numba import vectorize, cuda
from multiprocessing import Process

from makeDefaultParams import makeDefaultParams
from computeTemporalFiltering import computeTemporalFiltering
from normalizeImage import  normalizeImage
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
tf.enable_eager_execution()
import cv2
import matplotlib.pyplot as plt
if __name__ == '__main__':


    # with h5py.File('./video_explosion.mat', 'r') as f:
         # video = tf.constant(np.transpose(f['video'],[1,0,3,2]))
    
    params = makeDefaultParams(1e5)
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,308)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,308)
    #cap= cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)308, height=(int)308,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    sm = pySaliencyMap.pySaliencyMap(308,308)
    r_s = np.flip(makeTemporalFilter('strong_t3'),axis=-1)
    r_w = np.flip(makeTemporalFilter('weak_t6'),axis=-1)
    
    #r_s = tf.convert_to_tensor(
    #r_w = tf.convert_to_tensor(np.reshape(np.flip(makeTemporalFilter('strong_t3'),axis=-1)
    fil_s = tf.to_double(np.reshape(r_s, [3, 1, 1, 1, 1]))
    fil_w = tf.to_double(np.reshape(r_w, [6, 1, 1, 1, 1]))
    video =[]
    ret, frame = cap.read()
    if ret:
        print("Camera found")
    fr_no = 0
    
    #sess = tf.Session()
    #video = np.zeros((10,608,608,3))
    
    while (True):
        video = []
        # Capture frame-by-frame
        for i in range(6):
            ret, frame = cap.read()
            video.append(frame)
        st = time.time()
        #temp_frames = tf.expand_dims(video,axis=-1)
        print("pop:",time.time()-st)
        start = time.time()
        #video = np.transpose(np.asarray(video),[1,2,3])
        #print("Video shape:"+str(video.shape))
        
        #temp_out_strong, temp_out_weak = computeTemporalFiltering(video,params)
        temp_out_strong, temp_out_weak = ComputeTemporalFilter_jam(video,fil_s,fil_w)
        print("Temporal_Filter :",time.time()-start,"/n")
        # size(frames,1),size(frames,2),3,numel(params.channels)
        imgs = np.zeros((video[0].shape[0], video[0].shape[1], video[0].shape[2], len(params['channels'])))

        for l in range(temp_out_strong.shape[3]):
            # for l in range(1):
            start = time.time()

            imgs[:, :, :, 0] = normalizeImage((tf.squeeze(temp_out_strong[l, :, :, :])))
            imgs[:, :, :, 1] = normalizeImage((tf.squeeze(temp_out_weak[ l,:, :, :])))
            imgs[:, :, :, 2] = normalizeImage(video[l])
    # ChannelFirst
    # img = generateChannels(imgs,params)
            R, G, B, inp = generateChannels(imgs, params)

            salmap = sm.sal_map(R, G, B,inp)
            cv2.imshow('frame', cv2.bitwise_not(salmap))
    #cv2.waitKey()
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            print("map_time:",time.time()-start,"\n")
    # cv2.imwrite("C:/Users/Sathyaprakash/Desktop/python/images/"+"frame_"+str(l)+".jpg", salmap)
            # plt.imsave("/media/yesh/c6023e6a-3832-4c3c-9f34-5e3c280e1f20/yesh_friend/python/images/"+"frame_"+str(fr_no)+".png",salmap,cmap='jet')
            fr_no = fr_no +1
            # plt.show()
            # cv2.waitKey()
            #print(np.max(max(salmap)))
            

        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        # cv2.imshow('frame', gray)
        #     if cv2.waitKey(1) & 0xFF == ord('q'):
        #         break




        # [b1Pyr,b2Pyr] = makeBorderOwnership(img,params)
        #
        # # static(normalizeImage(tf.squeeze(temp_out_strong[:, l, :, :])))
        # print(time.time()-start)
        #
        # plt.imshow(0.33 *imgs[:,:,2])

        # plt.imshow(0.33*np.sum(imgs[:,:,2]))#,-1))




        # img = tf.add(imgs,axis=)
