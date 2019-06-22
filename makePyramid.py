

# import tensorflow as tf
import numpy as np
import cv2
def makePyramid(img,params):
    
    depth = params['maxLevel']
    pyr = {'data': []}

    pyr['data'].append(np.asarray(img))

    for l in range(1,depth):


        if (params['csPrs']['downSample']== 'half'): # downsample halfoctave
            pyr['data'].append( cv2.resize(
                pyr['data'][l - 1],
                width=int(np.ceil(pyr['data'][l-1].shape[0]*0.70833)),height=int(np.ceil(pyr['data'][l-1].shape[1]*0.70833)),
                interpolation=cv2.Interpolation.CUBIC
            ))



        elif (params['csPrs']['downSample']== 'full'): # downsample

            pyr['data'][l] = cv2.resize(
                pyr['data'][l - 1],
                width=pyr['data'][l - 1].shape[0] * 0.5, height=pyr['data'][l - 1].shape[1] * 0.5,
                interpolation=cv2.Interpolation.CUBIC
            )

        else:
            print('Please specify if downsampling should be half or full octave')


    return pyr