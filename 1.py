import cv2
import  numpy as np


# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)
#



cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("viedo",img)
    if cv2.waitKey(1)&0xFF == ord('q'):
        break



####################


# img = cv2.imread("Resources/lena.png")
#
# kernel = np.ones((5,5),np.uint8)
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
# imgBlur = cv2.GaussianBlur(imgGray,(3,3),1)
#
# imgcanny = cv2.Canny(img,100,100)
#
# imgDialation = cv2.dilate(imgcanny,kernel,iterations=1)
#
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
#
#
# cv2.imshow("gray image", imgGray)
#
# cv2.imshow("blur image", imgBlur)
# cv2.imshow("canny image", imgcanny)
# cv2.imshow("dialation image", imgDialation)
# cv2.imshow("Eroded image", imgEroded)
# cv2.waitKey(0)


#################################################



# img = cv2.imread("Resources/lambo.png")
# print(img.shape)
#
# imgresize = cv2.resize(img,(224,224))
# print(imgresize.shape)
#
# imgcrop = img[0:200,200:500]
#
#
# cv2.imshow("Output",img)
# cv2.imshow("Output1",imgresize)
# cv2.imshow("Output2",imgcrop)
# cv2.waitKey(0)

######################################################

# img = np.zeros((512,512))

#
# img = cv2.imread("Resources/lambo.png")
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3)
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),40)
# cv2.circle(img,(400,50),10,(255,255,0),5)
#
# cv2.putText(img,"OPENCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)
#
#
#
# cv2.imshow("image",img)
# cv2.waitKey(0)

###########################################################################

# img = cv2.imread("Resources/cards.jpg")
#
# width,height = 250,350
# pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
# pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
# matrix = cv2.getPerspectiveTransform(pts1,pts2)
# imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#
#
# cv2.imshow("Image",img)
# cv2.imshow("Output",imgOutput)
#
# cv2.waitKey(0)

##############################################################################



