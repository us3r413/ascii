import pygame
import curses
import time
import currentfile as cf
filename = cf.file()
fps = cf.fps()
frame = cf.frame()
pygame.init()
pygame.mixer.init()
def main(stdscr):
    global fps,frame,filename
    spf = 1.0/fps
    pygame.mixer.music.load(fr".\{filename}\{filename}.wav")
    i=0
    start_time=time.time()
    pygame.mixer.music.play()
    while(1):
        duration=time.time()-start_time
        f = open(fr".\frames\frame_{int(duration/spf)}.txt","r")
        output=f.read()
        f.close()
        stdscr.clear()
        stdscr.addstr(output)
        stdscr.refresh()
    pygame.mixer.music.unload()
if __name__ == "__main__":
    curses.wrapper(main)
