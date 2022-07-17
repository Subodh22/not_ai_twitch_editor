 
import cvzone
import cv2 
import numpy as np 
import os
import glob
import random
from matplotlib import pyplot as plt
imgback = cv2.imread('./Streamer_head/black.png')

 
def image_overlay(img1,img2,location):
    h,w =img1.shape[:2]
    h1,w1 = img2.shape[:2]
    x,y = location
    img1[y:y+h1,x:x+w1]= img2
    return img1

def thumb_maker(head,ass,name,streamer):

    cal= random.choice([0,700])
    asse=ass.split('.')
 
    imgfronty=cv2.imread('C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\thumbnails_bg\\'+streamer+'\\'+ass,cv2.IMREAD_UNCHANGED)
    imgfront_x=cv2.imread('C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\Streamer_head\\'+streamer+'\\'+head,cv2.IMREAD_UNCHANGED)
    imgfront_x = cv2.resize(imgfront_x,(250,333),None,1 ,1 )
    imgfronty = cv2.resize(imgfronty,(1200,675),None,1 ,1 )
    imgResult= image_overlay(imgback,imgfronty,location=(30,30))
    imgfront_x = cv2.resize(imgfront_x,(0,0),None,2.5,2.5 )
    imglast=cvzone.overlayPNG(imgResult,imgfront_x,[cal,30])
    cropped_image = imglast[20:720, 100:1280]
    cv2.imwrite('C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\act_thumbnails\\'+streamer+'\\'+asse[0]+'.png',cropped_image)
   

def mainer(streamer):
    os.chdir('C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\thumbnails_bg\\'+streamer)
    files = glob.glob("./*")
    files.sort(key=os.path.getmtime)
    os.chdir("..")

    for i in range(len(files)):
        s=os.path.basename(files[i])
        w=random.choice(os.listdir('C:\\Users\\Subodh Maharjan\\Desktop\\videoeditor\\Streamer_head\\'+streamer))
    
        thumb_maker(w,s,i,streamer)

 
if __name__=="__main__":
      
   pass

 
