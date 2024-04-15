import cv2
import sys
sys.path.insert(0, '..\..\project_ASCII')
import currentfile as cf
filename = cf.file()
h = cf.h()
def resize(frame):
    global h
    height, width, _ = frame.shape
    ratio = width/height
    new_width = int(h*ratio)
    resized_image = cv2.resize(frame, (new_width,h))
    return (resized_image,new_width)
def main():
    global h
    new_height = h
    filename = cf.file()
    vidcap = cv2.VideoCapture(fr"..\{filename}\{filename}.mov")
    success,image_1 = vidcap.read()
    number=0
    counter = 0
    while success:
        image_1,k = resize(image_1)
        frame = ''
        for y in range(0,new_height):
            for x in range(0,k):
                b,g,r = image_1[y][x]
                if (number!=0):
                    bl,gl,rl = image_2[y][x]
                    if ((b==bl)&(g==gl)&(r==rl)&(x!=k-1)):
                        counter+=2
                        continue
                    if (counter!=0|((x==k-1)&counter!=0)):
                        frame += f'\033[{counter}C'
                        counter=0
                frame += f'\033[38;2;{r};{g};{b};48;2;0;0;0mEE'
            frame+='\n'
        name = f"frame_{number}.txt"
        with open(name, 'x') as f:
            f.write(frame)
        image_2=image_1
        success,image_1 = vidcap.read()
        number+=1
        


if __name__ == "__main__":
    main()