import cv2 as cv
import curses
import time
import pygame
#ASCII character for grayscale to ascii conversion
ASCII_CHARS=['  ','  ','::','--','==','++','**','##',r'%%','@@']
#resized frame to grayscale
def grayify(frame):
    blackandwhite = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    return blackandwhite
#resize frame
def resize(frame, new_height=110):
    height, width, _ = frame.shape
    ratio = width/height
    new_width = int(new_height*ratio)
    resized_image = cv.resize(frame, (new_width,new_height))
    return (resized_image)
#grayscale to ascii
def convert(frame):
    ascii_frame = []
    LOCAL_CHARS = ASCII_CHARS
    for row in frame:
        for pixel in row:
            ascii_frame += LOCAL_CHARS[int((pixel / 256) * 9)]
        ascii_frame += '\n'
    return ascii_frame
#video to frame
def main(stdscr):
    vidcap = cv.VideoCapture(r"hiasobi-miku.mp4")
    success,image = vidcap.read()
    fps = vidcap.get(cv.CAP_PROP_FPS)
    spf = 1.0 / fps
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r"hiasobi-miku.wav")
    pygame.mixer.music.play()
    while success:
        start_time = time.time()
        newframe=resize(image)
        newframe=grayify(newframe)
        ascii_frame = convert(newframe)
        output = ''.join(ascii_frame)
        stdscr.clear()
        stdscr.addstr(output)
        stdscr.refresh()
        k = spf+start_time
        delay_time = max(k - time.time(), 0)
        time.sleep(delay_time)
        success,image = vidcap.read()
    pygame.mixer.music.unload()

curses.wrapper(main)