
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
from normalizeImage import  normalizeImage

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
    #cap = cv2.VideoCapture(1)
    cap = cv2.VideoCapture(1)
    #cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
    #cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)
    width  = 640
    height = 480
    saliency = cv2.saliency.MotionSaliencyBinWangApr2014_create()
    saliency.setImagesize(width, height)
    saliency.init()
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
    l = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    while (l):
        
        
        st = time.time()
        video = np.asarray(video)
      
        temp_out_strong, temp_out_weak = ComputeTemporalFilter_jam(video,r_s,r_w)
     

        #imgs[:,:,0] =  cv2.cvtColor(normalizeImage(temp_out_strong),cv2.COLOR_BGR2GRAY)
        #imgs[:,:,:,1] = normalizeImage(temp_out_weak)
        #imgs[:,:,:,2] = normalizeImage(video[2])

        #R, G, B, inp = generateChannels(imgs, params)
        (success, saliencyMap) = saliency.computeSaliency(cv2.cvtColor(normalizeImage(frame),cv2.COLOR_BGR2GRAY))
        #(success, saliencyMap) = saliency.computeSaliency(imgs[:,:,0])
        #(success, saliencyMap2) = saliency.computeSaliency( cv2.cvtColor(imgs[:,:,:,1], cv2.COLOR_BGR2GRAY))
        #(success, saliencyMap3) = saliency.computeSaliency( cv2.cvtColor(imgs[:,:,:,2], cv2.COLOR_BGR2GRAY))
        #saliencyMap = (saliencyMap1 * 255).astype("uint8")+(saliencyMap2 * 255).astype("uint8")+(saliencyMap3 * 255).astype("uint8")
	# display the image to our screen
        cv2.imshow("Frame", frame)
        cv2.imshow("Map", cv2.applyColorMap(saliencyMap, cv2.COLORMAP_JET))
        key = cv2.waitKey(1) & 0xFF
        print("FPS:",1/(time.time()-st))
        #if cv2.waitKey(1) == 27: 
        #    break  # esc to quit
        video[:5,:,:,:] = video[1:,:,:,:]
        ret, frame = cap.read()
        video[5,:,:,:]= frame
        l =  l-1
    
        #print("map_time:",time.time()-st,"\n")
    cv2.destroyAllWindows()
    

        # img = tf.add(imgs,axis=)
