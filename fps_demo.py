import cv2
import sal
import time
#import sal
import numpy as np
from normalizeImage import normalizeImage
params = sal.makeDefaultParameters(1e5)
cap = cv2.VideoCapture(1)
width  = 640
height = 480
sm = sal.pySaliencyMap(height,width)
r_s = np.reshape(sal.makeTemporalFilter('strong_t3'), (3,1,1,1))
r_w = np.reshape(sal.makeTemporalFilter('weak_t6'), (6,1,1,1))
imgs = np.zeros((height,width,3,3))
video = np.zeros((6,height,width,3))
for i in range(6):
    ret, frame = cap.read()
    print(np.asarray(frame).shape)
    video[i,:,:,:]= frame

video = np.asarray(video)
print("IM:",np.asarray(imgs).shape)
while True:
    # Capture frame-by-frame
    
    video[:5,:,:,:] = video[1:,:,:,:]
    ret, frame = cap.read()
    video[5,:,:,:]= frame
    
    temp_out_strong, temp_out_weak = sal.ComputeTemporalFilter_jam(video,r_s,r_w)
    print("sal:",np.asarray( imgs[:,:,:,0]).shape)
    imgs[:,:,:,0] = sal.normalizeImage(temp_out_strong)
    imgs[:,:,:,1] = sal.normalizeImage(temp_out_weak)
    imgs[:,:,:,2] = sal.normalizeImage(video[2])
    # ChannelFirst
    # img = generateChannels(imgs,params)
    R, G, B, inp = sal.generateChannels(imgs, params)

    salmap = sm.sal_map(R, G, B,inp)
    

    # Display the resulting frame
    cv2.imshow('Video', salmap)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
