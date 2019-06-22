import cv2
import numpy as np
from genBump import genBump
#from PIL import Image
#from __future__ import divison
import time 
def read_cam():

    sens = genBump(3, 608, 608, 13)
    cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)608, height=(int)608,format=(string)I420, framerate=(fraction)120/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")
    if cap.isOpened():
        windowName = "CannyDemo"
        cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(windowName,1280,720)
        cv2.moveWindow(windowName,0,0)
        cv2.setWindowTitle(windowName,"Canny Edge Detection")
        #print "camera ready"
        counter = 0
        images = []
        img_nm = 1
        img_nm_r = 1
	
        while True:
            #start = time.time()
            ret_val, frame = cap.read()
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            #cv2.imwrite("/home/nvidia/Desktop/CS/frames/"+str((str(img_nm_r))+".jpg"),gray_frame)
            img_nm_r = img_nm_r + 1
	    
            if(counter==13):
        


	        image_list = np.asarray(images)
		compressed_image = np.multiply(sens, image_list)
		compressed_image = np.sum(compressed_image, 0)/3.

		compressed_image = np.array(compressed_image, dtype=np.uint8)
	#	cv2.imwrite("/home/nvidia/Desktop/CS/compressed_frames/"+str((str(img_nm))+".png"),compressed_image)
		img_nm = img_nm + 1
		cv2.imshow(windowName,compressed_image)
	    #	        compressed_image = cv2.cvtColor(compressed_image, cv2.COLOR_GRAY2BGR)
		counter = 0
		images=[]
		continue
		images.append(gray_frame)
		counter = counter + 1	
		end = time.time()
		print(str(end-start),"\n",counter)
		    
		key=cv2.waitKey(10)
		if key == 27: # Check for ESC key
		    cv2.destroyAllWindows()
		    break ;
    else:
        print "camera opening failed!"



if __name__ == '__main__':
    read_cam()
