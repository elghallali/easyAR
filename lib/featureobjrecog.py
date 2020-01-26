import numpy as np 
import cv2
import os
from lib.objloader_simple import *

# fature based object recongnition including feature extraction feature description and matching 
class FBORecognition :


    def __init__ (self):
        self.orb = None
        self.model = None
        self.obj = None
        self.bf = None
    
    def orbDetector(self,  model="", dobject=""):
        self.orb = cv2.ORB_create()
        # create BFMatcher object based on hamming distance  
        self.bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # load the reference surface that will be searched in the video stream
        dir_name = os.getcwd()
        self.model = cv2.imread(os.path.join(dir_name, model), 0)
        # Compute model keypoints and its descriptors
        kp_model, des_model = self.orb.detectAndCompute(self.model, None)
        # Load 3D model from OBJ file
        self.obj = OBJ(os.path.join(dir_name, dobject), swapyz=True)