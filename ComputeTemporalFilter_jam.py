import numpy as np
import scipy.signal as sc

time = 6
def ComputeTemporalFilter_jam(video,r_s,r_w):

    temp_strong = np.sum(video[1:4]*r_s,axis=0)
    temp_weak = np.sum(video*r_w,axis=0)

    return temp_strong,temp_weak
	
	
