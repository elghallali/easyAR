import numpy as np 
import cv2 

class Camera :

    def __init__(self):
        print("Camera Constructor")
        self.cap = cv2.VideoCapture(0)

    def steam(self) :
        while(True):
            # Capture frame-by-frame
            ret, frame = self.cap.read()
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
            
            # Display the resulting frame
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        # When everything done, release the capture
        self.cap.release()
        cv2.destroyAllWindows()
