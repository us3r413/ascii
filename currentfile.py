import cv2
filename = "hiasobi-miku"
video = cv2.VideoCapture(fr".\{filename}\{filename}.mov")
def file ():
    return filename
def fps ():
    return video.get(cv2.CAP_PROP_FPS)
def frame ():
    return int(video.get(cv2.CAP_PROP_FRAME_COUNT))
def h ():
    return 110
