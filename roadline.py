import cv2
import numpy as np
from attr.validators import min_len
from pyrealsense2 import region_of_interest
from scipy.special import betaln

cap=cv2.VideoCapture("C:/Users/Jesse/Desktop/RoadLineDetection/.mp4")
def drawLines(img,Lines):
    image=np.copy(img)
    blank_img=np.zeros((image.shape[0],image.shape[1],3),dtype=np.uint8) # Boş bir görüntü oluşturmak için kullanılır. Siyah bir görüntü
    if Lines is not None:
        for line in Lines:
            for x1,y1,x2,y2 in line:
                cv2.line(blank_img,(x1,y1),(x2,y2),(0,255,0),thickness=8)
    image=cv2.addWeighted(image,1,blank_img,1,0.0)
    return image


def process(img):
    height, width = img.shape[0], img.shape[1]
    region_of_interest_vertices=[(0,height),(width/2,height/2.5),(width,height)]
    gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    canny_image=cv2.Canny(img,150,250)
    masked_image=region_of_interest(canny_image,np.array([region_of_interest_vertices],np.int32))
    lines=cv2.HoughLinesP(masked_image,rho=2,theta=np.pi/180,threshold=100,lines=np.array([]),minLineLength=100,maxLineGap=10)
    imageWithLine=drawLines(img,lines)
    return imageWithLine


def region_of_interest(img,vertices):
    mask=np.zeros_like(img)
    match_mask_color=255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image=cv2.bitwise_and(img,mask)
    return masked_image



while True:
    success, img=cap.read()
    if success:
        img = process(img)
        cv2.imshow(" ",img)
        cv2.waitKey(20)
    else:
        print("line göremedi")
        break

cap.release()
cv2.destroyAllWindows()