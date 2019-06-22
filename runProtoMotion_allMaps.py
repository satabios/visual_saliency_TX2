
import cv2
from makeDefaultParams import makeDefaultParams

def runProtoMotion_allMaps(video, w):


    print("Start Proto-Object Saliency")

    params = makeDefaultParams(w)


    return h

def main():

    cap = cv2.VideoCapture('10.mp4')
    video = []

    for i in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):

        ret, frame = cap.read()
        video.append(frame)
    sal = runProtoMotion_allMaps(video,100000)




