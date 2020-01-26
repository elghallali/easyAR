#halper libraries
import argparse
import numpy as np 
#opencv library
import cv2
# pygame library and open cv screen
from lib.camera import *
from lib.pygamescene import *
from lib.marker import *


def main() : 
    print("=================The main Method of AR Application=================")
    tenser = MarkerDetection()
    #camera = Camera()
    #camera.steam()
    pg = ArPyGameScene()
    pg.steam()


if __name__ == '__main__':
    main()