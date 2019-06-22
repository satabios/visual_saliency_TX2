
import tensorflow as tf
from makeTemporalFilter import  makeTemporalFilter
import numpy as np
# from cuda_chk import con
import scipy.signal



def computeTemporalFiltering(frames,w):

    r_s = np.flip(makeTemporalFilter('strong_t3'),axis=-1)
    r_w = np.flip(makeTemporalFilter('weak_t6'),axis=-1)
    
    #r_s = tf.convert_to_tensor(
    #r_w = tf.convert_to_tensor(np.reshape(np.flip(makeTemporalFilter('strong_t3'),axis=-1)
    fil_s = tf.to_double(np.reshape(r_s, [3, 1, 1, 1, 1]))
    fil_w = tf.to_double(np.reshape(r_w, [6, 1, 1, 1, 1]))
    #cv2.namedWindow('frame')



    

    temp_frames = tf.expand_dims(frames,axis=-1)
   

    temporal_out_s = tf.nn.conv3d(
        tf.to_double(temp_frames),
        fil_s,
        strides=[1, 1, 1, 1, 1],
        padding='SAME',

    )

    temporal_out_w = tf.nn.conv3d(
        tf.to_double(temp_frames),
        fil_w,
        strides=[1, 1, 1, 1, 1],
        padding='SAME',

    )







    return (temporal_out_s,temporal_out_w)
