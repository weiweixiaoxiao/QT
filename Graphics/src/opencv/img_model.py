import cv2  
import numpy as np 
from matplotlib import pyplot as plt
#图像轮廓检测 
img = cv2.imread('file/lotus.jpg')  
cv2.imshow("img", img)  
cv2.waitKey(0) 

#图片轮廓检测
def outline():
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  
    ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)  
      
    _,contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)  
    cv2.drawContours(img,contours,-1,(0,0,255),3)  
      
    cv2.imshow("img", img)  
    cv2.waitKey(0)  
    
#放大图片
def magnify():
    # 沿着横纵轴放大1.6倍，然后平移(-150,-240)，最后沿原图大小截取，等效于裁剪并放大
    M_crop_elephant = np.array([
        [1.6, 0, -150],
        [0, 1.6, -240]
    ], dtype=np.float32)
    
    img_magnify = cv2.warpAffine(img, M_crop_elephant, (400, 600))
    cv2.imshow("img_elephant", img_magnify)  
    cv2.waitKey(0)  
    #cv2.imwrite('file/lotusFangda.jpg', img_magnify)

#图像倾斜  
def sheared():
    # x轴的剪切变换，角度15°
    theta = 15 * np.pi / 180
    M_shear = np.array([
        [1, np.tan(theta), 0],
        [0, 1, 0]
    ], dtype=np.float32)
    
    img_sheared = cv2.warpAffine(img, M_shear, (400, 600))
    cv2.imshow("img_elephant", img_sheared)  
    cv2.waitKey(0)  
    #cv2.imwrite('lanka_safari_sheared.jpg', img_sheared)
    
#图像旋转
def rotated():
    rows,cols,channel = img.shape
    M = cv2.getRotationMatrix2D((cols/2,rows/3),90,0.4)
    dst = cv2.warpAffine(img,M,(cols,rows))
     
    cv2.imshow('img',dst)
    cv2.waitKey(0)
    #cv2.imwrite('lanka_safari_rotated.jpg', img_rotated)

#图像平移
def translation():
    rows,cols,channel = img.shape
    M = np.float32([[1,0,100],[0,1,50]])
    dst = cv2.warpAffine(img,M,(cols,rows))
    cv2.imshow('img',dst)
    cv2.waitKey(0)
    #cv2.destroyAllWindows()

#图像仿射变换 仿射变换是一种二维坐标到二维坐标之间的线性变换，并保持二维图形的“平直性”。转换前平行的线，在转换后依然平行
def affine():
    rows,cols,channel = img.shape
 
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10,100],[200,50],[100,250]])
     
    M = cv2.getAffineTransform(pts1,pts2)
     
    dst = cv2.warpAffine(img,M,(cols,rows))
     
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()

#透视变换
def perspective():
    rows,cols,ch = img.shape 
    pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
     
    M = cv2.getPerspectiveTransform(pts1,pts2)
     
    dst = cv2.warpPerspective(img,M,(300,300))
     
    plt.subplot(121),plt.imshow(img),plt.title('Input')
    plt.subplot(122),plt.imshow(dst),plt.title('Output')
    plt.show()
    
#图片按比例放大缩小
def zoom():
#     res1 = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_CUBIC)
#     cv2.imshow("res1", res1)   
    img_200x300 = cv2.resize(img, (0, 0), fx=1.5, fy=1.5, 
                              interpolation=cv2.INTER_NEAREST)
    cv2.imshow('img_200x300', img_200x300) 
    cv2.waitKey(0)
    
outline()