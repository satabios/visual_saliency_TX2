import cv2
import numpy as np
from genBump import genBump
import time
import glob
#from __future__ import divison

def compress(imageList,sens):
  
   
  
    print(len(imageList))
    total_images = len(imageList)
    num_sets = int(total_images/13)
    bumpSize = 3
    #[RowSize, ColSize] = imageList[0].shape
    imageList = np.asarray(imageList)
    sens_matrix = sens
    compressed_image_list = np.zeros((1,608,608 ))
    # image_set = imageList[:, :, :]
    imageList = np.asarray(imageList)
    compressed_image = np.multiply(sens,imageList )
    compressed_image = np.sum(compressed_image, 0)/3
    compressed_image = np.asarray(compressed_image)
    cv2.imwrite("/home/satabios/Desktop/CS/frames/bg"+".jpg",compressed_image)
    # compressed_image_list[i, :, :] = compressed_image



def apend_images():
    print("apend__images")
    sens = genBump(3, 608, 608, 13)
    file_dir = '/home/satabios/Desktop/CS/frames/'
    cnt = 318
    img = []
    filename='/home/satabios/Desktop/CS/frames/'
    for i in range(cnt,331):
        files = filename + str(i) + '.jpg'
        print(str(files))
        cnt = cnt + 1
        
        frames = cv2.imread(files,0)
        #cv2.imwrite("./bg"+".png",frames)
        # cv2.imshow('frames',frames)
        # cv2.waitKey()
        img.append(frames)
        #img.append(imgs)
        if(cnt == 331):
            print(len(img))
            #img_set = np.asarray(img)
            
            compress(img,sens) 
            
            img = []

             
def read_cam():

    sens = genBump(3, 608, 608, 20)
    cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)608, height=(int)608,format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    if cap.isOpened():
        windowName = "CannyDemo"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(windowName,1280,720)
        cv2.moveWindow(windowName,0,0)
        cv2.setWindowTitle(windowName,"Canny Edge Detection")
        print ("camera ready")
        counter = 0
        images = []
        ret_val,frame=cap.read()
        displayBuf = frame
        while True:
            start = time.time()
            ret_val, frame = cap.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imwrite("/home/nvidia/Desktop/CS/frames/"+str(counter)+".png",gray_frame)
            images.append(gray_frame)
            counter = counter + 1
            if(counter==20):
                image_list = np.asarray(images)
                compressed_image = np.multiply(sens, image_list)
                compressed_image = np.sum(compressed_image, 0)/3.
        #compressed_image = np.array(compressed_image, dtype=np.uint8)
#           compressed_image = cv2.cvtColor(compressed_image, cv2.COLOR_GRAY2BGR)
                counter = 0
                displayBuf = compressed_image
                images=[]
                cv2.imshow(windowName,displayBuf)
                end = time.time()
                print(str(end-start))
        
                key=cv2.waitKey(10)
            if key == 27: # Check for ESC key
                cv2.destroyAllWindows()
                break ;
    else:
    
        print ("camera opening failed!")



if __name__ == '__main__':
    #read_cam()
    apend_images()