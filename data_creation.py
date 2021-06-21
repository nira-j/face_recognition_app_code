import cv2
import time
cap=cv2.VideoCapture(0)
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

for i in range(10):
    ret,photo=cap.read()
    gray_image=cv2.cvtColor(photo,cv2.COLOR_BGR2GRAY)
    face=model.detectMultiScale(gray_image)
    if len(face)==0:
        continue
    x=face[0][0]
    y=face[0][1]
    w=face[0][2]
    h=face[0][3]
    det_image=cv2.rectangle(gray_image,(x,y),(x+w,y+h),(127,0,255),2)
    croped_image=gray_image[y:y+w, x:x+h]
    croped_image=cv2.resize(croped_image,(200,200))
    
    path=f"./myimg/myimage{i}.jpg"
    cv2.imwrite(path,croped_image)
    cv2.putText(croped_image,"captured",(20,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
    cv2.imshow(path,croped_image)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    
cap.release()