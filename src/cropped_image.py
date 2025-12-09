import cv2 as cv
import numpy as np


path = r"C:\Users\gowth\Downloads\goku_4k_wallpaper_.jpg"

img = cv.imread(path)
draw = False
p1 = (0,0)
p2 = p1



def Mousecall(event,xpos,ypos,flags,param):
    global draw,p1,p2

    if event == cv.EVENT_LBUTTONDOWN:
        draw = True
        p1 = (xpos,ypos)
        p2 = p1
    if event == cv.EVENT_MOUSEMOVE and draw:
        p2 = (xpos,ypos)
    if event  == cv.EVENT_LBUTTONUP:
        draw = False
        
        (x1,y1) = p1
        (x2,y2) = p2
        xmin = min(p1[0],p2[0])
        ymin = min(p1[1],p2[1])
        xmax = max(p1[0],p2[0])
        ymax = max(p1[1],p2[1])
        if xmin<xmax and ymin<ymax:
            img_crp = img[ymin:ymax,xmin:xmax]
            cv.imshow('op2',img_crp)
            cv.imwrite(r"C:\Users\gowth\OneDrive\Desktop\work\opencv\croppedimg.jpg",img_crp)
        cv.rectangle(img, p1, (xpos, ypos), (0, 255, 0), 3)    


cv.namedWindow('frame')
cv.setMouseCallback('frame',Mousecall)


while True:
    img_display = img.copy()
    if draw:
        cv.rectangle(img_display,p1,p2,(0,255,0),3)
    cv.imshow('frame',img_display)
    key = cv.waitKey(1) & 0xff
    if key == ord('q'):
        break

cv.destroyAllWindows()
