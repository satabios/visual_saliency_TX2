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
import tensorflow as tf
tf.enable_eager_execution()
import cv2
import matplotlib.pyplot as plt
if __name__ == '__main__':

    a = sal_map()
    # # with h5py.File('./video_explosion.mat', 'r') as f:
    #      # video = tf.constant(np.transpose(f['video'],[1,0,3,2]))
    #
    # params = makeDefaultParams(1e5)
    # cap= cv2.VideoCapture("/media/yesh/c6023e6a-3832-4c3c-9f34-5e3c280e1f20/yesh_friend/python/sall_skiing.mp4")
    # sm = pySaliencyMap.pySaliencyMap(cap.read()[1].shape[0],cap.read()[1].shape[1])
    # video =[]
    # fr_no = 0
    # while (True):
    #     video = []
    #     # Capture frame-by-frame
    #     for i in range(10):
    #         ret, frame = cap.read()
    #         video.append(frame)
    #     start = time.time()
    #     temp_out_strong, temp_out_weak = computeTemporalFiltering(video, params)
    #     # sess = tf.Session()
    #     # size(frames,1),size(frames,2),3,numel(params.channels)
    #     imgs = np.zeros((video[0].shape[0], video[0].shape[1], video[0].shape[2], len(params['channels'])))
    #
    #     for l in range(temp_out_strong.shape[3]):
    #         # for l in range(1):
    #         start = time.time()
    #
    #         imgs[:, :, :, 0] = normalizeImage(tf.squeeze(temp_out_strong[l, :, :, :]))
    #         imgs[:, :, :, 1] = normalizeImage(tf.squeeze(temp_out_weak[ l,:, :, :]))
    #         imgs[:, :, :, 2] = normalizeImage(video[l])
    #         # ChannelFirst
    #         # img = generateChannels(imgs,params)
    #         R, G, B, inp = generateChannels(imgs, params)
    #
    #         salmap = sm.sal_map(R, G, B,inp)
    #         print("time:",time.time()-start,"\n")
    #         # cv2.imwrite("C:/Users/Sathyaprakash/Desktop/python/images/"+"frame_"+str(l)+".jpg", salmap)
    #         plt.imsave("/media/yesh/c6023e6a-3832-4c3c-9f34-5e3c280e1f20/yesh_friend/python/images/"+"frame_"+str(fr_no)+".png",salmap,cmap='jet')
    #         fr_no = fr_no +1
    #         # plt.show()
    #         # cv2.waitKey()
    #
    #     # Our operations on the frame come here
    #     # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #
    #     # Display the resulting frame
    #     # cv2.imshow('frame', gray)
    #     #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #     #         break
    #
    #
    #
    #
    #     # [b1Pyr,b2Pyr] = makeBorderOwnership(img,params)
    #     #
    #     # # static(normalizeImage(tf.squeeze(temp_out_strong[:, l, :, :])))
    #     # print(time.time()-start)
    #     #
    #     # plt.imshow(0.33 *imgs[:,:,2])
    #
    #     # plt.imshow(0.33*np.sum(imgs[:,:,2]))#,-1))
    #
def sal_map():




    # with h5py.File('./video_explosion.mat', 'r') as f:
         # video = tf.constant(np.transpose(f['video'],[1,0,3,2]))

    params = makeDefaultParams(1e5)
    cap= cv2.VideoCapture("/media/yesh/c6023e6a-3832-4c3c-9f34-5e3c280e1f20/yesh_friend/python/sall_skiing.mp4")
    sm = pySaliencyMap.pySaliencyMap(cap.read()[1].shape[0],cap.read()[1].shape[1])
    video =[]
    fr_no = 0
    while (True):
        video = []
        # Capture frame-by-frame
        for i in range(10):
            ret, frame = cap.read()
            video.append(frame)
        start = time.time()
        temp_out_strong, temp_out_weak = computeTemporalFiltering(video, params)
        # sess = tf.Session()
        # size(frames,1),size(frames,2),3,numel(params.channels)
        imgs = np.zeros((video[0].shape[0], video[0].shape[1], video[0].shape[2], len(params['channels'])))

        for l in range(temp_out_strong.shape[3]):
            # for l in range(1):
            start = time.time()

            imgs[:, :, :, 0] = normalizeImage(tf.squeeze(temp_out_strong[l, :, :, :]))
            imgs[:, :, :, 1] = normalizeImage(tf.squeeze(temp_out_weak[ l,:, :, :]))
            imgs[:, :, :, 2] = normalizeImage(video[l])
            # ChannelFirst
            # img = generateChannels(imgs,params)
            R, G, B, inp = generateChannels(imgs, params)

            salmap = sm.sal_map(R, G, B,inp)
            print("time:",time.time()-start,"\n")
            # cv2.imwrite("C:/Users/Sathyaprakash/Desktop/python/images/"+"frame_"+str(l)+".jpg", salmap)
            plt.imsave("/media/yesh/c6023e6a-3832-4c3c-9f34-5e3c280e1f20/yesh_friend/python/images/"+"frame_"+str(fr_no)+".png",salmap,cmap='jet')
            fr_no = fr_no +1
            # plt.show()
            # cv2.waitKey()

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
