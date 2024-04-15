import pygame
import time
import currentfile as cf
import sys
filename = cf.file()
fps = cf.fps()
frame = cf.frame()
pygame.init()
pygame.mixer.init()
def main():
    global fps,frame,filename
    d=fps
    pygame.mixer.music.load(fr".\{filename}\{filename}.wav")
    start_time=time.time()
    pygame.mixer.music.play()
    while(1):
        #modified after stress test
        duration=time.time()-start_time
        k=int(duration*d)
        #f = open(fr".\frames\frame_{int(duration/spf)}.txt","r")
        sys.stdout.write('\033[H'+ (open(fr".\frames\frame_{k}.txt","r")).read())
        #f.close()
        (open(fr".\frames\frame_{k}.txt","r")).close()
    pygame.mixer.music.unload()
if __name__ == "__main__":
    main()
    print('\033[0m\033[2J')