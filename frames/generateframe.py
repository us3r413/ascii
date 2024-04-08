import cv2 as cv
import sys
sys.path.insert(0, '..\..\project_ASCII')
import currentfile as cf
filename = cf.file()
#ASCII character for grayscale to ascii conversion
ASCII_CHARS=['  ','  ','..','::','--','==','++','**','##',r'%%','@@']
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
    for row in frame:
        for pixel in row:
            ascii_frame += ASCII_CHARS[int(pixel//25)]
        ascii_frame += '\n'
    return ascii_frame
#video to frame
def main():
    global filename
    vidcap = cv.VideoCapture(fr"..\{filename}\{filename}.mov")
    success,image = vidcap.read()
    number=0
    while success:
        newframe=resize(image)
        newframe=grayify(newframe)
        ascii_frame = convert(newframe)
        output = ''.join(ascii_frame)
        filename = f"frame_{number}.txt"
        with open(filename, 'w') as f:
            f.write(output)
        success,image = vidcap.read()
        number+=1
if __name__ == "__main__":
    main()