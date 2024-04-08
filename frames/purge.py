import os
import cv2
import sys
sys.path.insert(0, '..\..\project_ASCII')
import currentfile as cf
filename = cf.file()
vidcap = cv2.VideoCapture(fr"..\{filename}\{filename}.mov")
for i in range(0,int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))):
    if(os.path.exists(fr"frame_{i}.txt")):
        os.remove(fr"frame_{i}.txt")
    else:
        print(f"frame_{i}.txt doesn't exist")
        break