
import  tensorflow as tf
import numpy as np

def makeColors(imgs):
    # print('Generating color channels according to Itti et al (1998)\n')

    # imgs = np.asarray(imgs)
    im = imgs[:,:,:,1]
    r = im[:,:,0]
    g = im[:,:,1]
    b = im[:,:,2]

    inp = (r+ g + b)/ 3

    msk = np.copy(inp)
    msk[msk<0.1*np.max(np.max(inp))] = 0
    msk[msk!=0] = 1


    r = np.divide(r * msk, inp)
    g = np.divide(g * msk, inp)
    b = np.divide(b * msk, inp)

    R = r - (g + b) / 2
    R[R < 0] = 0

    G = g - (r + b) / 2
    G[G < 0] = 0

    B = b - (r + g) / 2
    B[B < 0] = 0

    Y = (r + g) / 2 - abs(r - g) / 2 - b
    Y[Y < 0] = 0


    im_orient = imgs[:,:,:,2]
    r_orient = im_orient[:,:,0]
    g_orient = im_orient[:,:,1]
    b_orient = im_orient[:,:,2]

    in_orient = (r_orient + g_orient + b_orient) / 3

    im = imgs[:,:,:,0]
    r = im[:,:,0]
    g = im[:,:,1 ]
    b = im[:,:,2]

    inp = (r + g + b) / 3



    return inp,in_orient,R,G,B,Y
