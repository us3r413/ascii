import cv2
import pygame
import curses
import time
def main(stdscr):
    vidcap = cv2.VideoCapture(r"badapple.mov")
    fps = vidcap.get(cv2.CAP_PROP_FPS)
    spf = 1.0/fps
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(r"badapplemusic.wav")
    for i in range(0,int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))):
        start_time = time.time()
        f = open(fr".\frames\frame_{i}.txt","r")
        output=f.read()
        f.close()
        stdscr.clear()
        if (i==0):
            pygame.mixer.music.play()
        stdscr.addstr(output)
        stdscr.refresh()
        k = spf+start_time
        delay_time = max(k - time.time(), 0)
        time.sleep(delay_time)
    pygame.mixer.music.unload()

curses.wrapper(main)