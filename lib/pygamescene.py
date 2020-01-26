import numpy as np 
import cv2 as cv2
import pygame
from pygame.locals import *
from lib.mian2dcharachter import *
from lib.main3dcharchter import *
import sys

class ArPyGameScene :


    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        print("Paygame AR scene initialization")
        pygame.init()
        pygame.display.set_caption("OpenCV camera stream on Pygame")
        self.screen = pygame.display.set_mode([1280,720])
        self.my_charcter = Mian2DCharachter()
        #creating a group with our sprite
        self.my_group = pygame.sprite.Group(self.my_charcter)
        #getting the pygame clock for handling fps
        self.clock = pygame.time.Clock()
        self.FPS = 10 #Frames per second
     
    def steam(self) :
        try : 
            while(True):
                ret, frame = self.cap.read()
                self.screen.fill([0,0,0])
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                #frame = cv2.flip(frame, 0)
                frame = frame.swapaxes(0,1)
                frame = pygame.surfarray.make_surface(frame)
                self.screen.blit(frame, (0,0))

                #find homography for object projextion cv2.findHomography
                # scene -----------------------------------------
                #updating the sprite of main charcter
                self.my_group.update()

                #drawing the sprite
                self.my_group.draw(self.screen)
        
                #------------------------------------------------
                
                pygame.display.update() # update all the scene

                #finally delaying the loop to with clock tick for 10fps 
                self.clock.tick(self.FPS)

                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        sys.exit(0)
        
        except (KeyboardInterrupt,SystemExit):
            pygame.quit()
            self.cap.release()
            cv2.destroyAllWindows()