import cv2
import Controlador
from cvzone.HandTrackingModule import HandDetector

detector=HandDetector(detectionCon=0.8,maxHands=1)

video=cv2.VideoCapture(0)

while True:
    ret,frame=video.read()
    frame=cv2.flip(frame,1)
    hands,img=detector.findHands(frame)
    if hands:
        lmList=hands[0]
        dedosArriba=detector.fingersUp(lmList)

        print(dedosArriba)
        Controlador.led(dedosArriba)
        if dedosArriba==[0,0,0,0,0]:
            cv2.putText(frame,'Conteo dedos:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif dedosArriba==[1,0,0,0,0]:
            cv2.putText(frame,'Conteo dedos:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)    
        elif dedosArriba==[1,1,0,0,0]:
            cv2.putText(frame,'Conteo dedos:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif dedosArriba==[1,1,1,0,0]:
            cv2.putText(frame,'Conteo dedos:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif dedosArriba==[1,1,1,1,0]:
            cv2.putText(frame,'Conteo dedos:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        elif dedosArriba==[1,1,1,1,1]:
            cv2.putText(frame,'Conteo dedos:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA) 

    cv2.imshow("Pantalla de Video",frame)
    q=cv2.waitKey(1)
    if q==ord("q"):
        break

video.release()
cv2.destroyAllWindows()