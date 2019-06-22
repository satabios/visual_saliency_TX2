
import cv2
import matplotlib.pyplot as plt
import matplotlib
import sal
import time
import numpy as np

if __name__ == '__main__':




    params = sal.makeDefaultParams(1e5)
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,300)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,300)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    #
    
    
    #cap= cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)308, height=(int)308,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    sm = sal.pySaliencyMap(height,width)
    
    r_s = np.reshape(sal.makeTemporalFilter('strong_t3'), (3,1,1,1))
    r_w = np.reshape(sal.makeTemporalFilter('weak_t6'), (6,1,1,1))
    imgs = np.zeros((height,width,3,3))
    print(r_s.shape)
  return R,G,B,inp
    st = time.time()
    video = np.zeros((6,height,width,3))
    for i in range(6):
            ret, frame = cap.read()
            print(np.asarray(frame).shape)
            video[i,:,:,:]= frame
    imgs = np.zeros((video[0].shape[0], video[0].shape[1], video[0].shape[2], len(params['channels'])))
    #plt.ion()
    salmap = np.zeros((height,width))
    #plt.title("Histogram")
    #cv2.namedWindow('frame')
    while (True):
        #video =[]
        #imgplt = plt.imshow(salmap)
        #plt.draw()
        # Capture frame-by-frame
        #st = time.time()
        video[:5,:,:,:] = video[1:,:,:,:]
        ret, frame = cap.read()
        video[5,:,:,:]= frame
        
        video = np.asarray(video)
        #print("Sahpe:",np.asarray(video).shape)
        #temp_frames = tf.expand_dims(video,axis=-1)
        #print("pop:",time.time()-st)
        #start = time.time()
        #video = np.transpose(np.asarray(video),[1,2,3])
        #print("Video shape:"+str(video.shape))
        
        #temp_out_strong, temp_out_weak = computeTemporalFiltering(video,params)
        temp_out_strong, temp_out_weak = sal.ComputeTemporalFilter_jam(video,r_s,r_w)
        #print("Temporal_Filter :",time.time()-start,"/n")
        
        # size(frames,1),size(frames,2),3,numel(params.channels)
        

        #for l in range(temp_out_strong.shape[3]):
            # for l in range(1):
        #start = time.time()

        imgs[:,:,:,0] = sal.normalizeImage(temp_out_strong)
        imgs[:,:,:,1] = sal.normalizeImage(temp_out_weak)
        imgs[:,:,:,2] = sal.normalizeImage(video[2])
    # ChannelFirst
    # img = generateChannels(imgs,params)
        R, G, B, inp = sal.generateChannels(imgs, params)

        salmap = sm.sal_map(R, G, B,inp)
        #plt.pause(0.00000001)
        #plt.clf()
        #cv2.imshow('frame',salmap)
        #plt.imshow(salmap)
        #plt.show()
        cv2.imshow('frame' ,salmap )
        #cv2.waitKey()
        print("FPS:",1/(time.time()-st))
        if cv2.waitKey(1) == 27: 
            break  # esc to quit
    
        #print("map_time:",time.time()-st,"\n")
    cv2.destroyAllWindows()
    # cv2.imwrite("C:/Users/Sathyaprakash/Desktop/python/images/"+"frame_"+str(l)+".jpg", salmap)
            # plt.imsave("/media/yesh/c6023e6a-3832-4c3c-9f34-5e3c280e1f20/yesh_friend/python/images/"+"frame_"+str(fr_no)+".png",salmap,cmap='jet')
            #fr_no = fr_no +1
            # plt.show()
            # cv2.waitKey()
            #print(np.max(max(salmap)))
            

        # Our operations on the frame come here
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        # cv2.imshow('frame', gray)ch
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
