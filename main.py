import argparse
import numpy as np 
import cv2
from lib.camera import *
from lib.pygamescene import *

def main() : 
    print("=================The main Method of AR Application=================")
    
    #camera = Camera()
    #camera.steam()
    pg = ArPyGameScene()
    pg.steam()


if __name__ == '__main__':
    main()