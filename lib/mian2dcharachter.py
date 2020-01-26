import pygame

class Mian2DCharachter(pygame.sprite.Sprite):
    def __init__(self):
        super(Mian2DCharachter ,self).__init__()
        self.images = []
        self.images.append(pygame.image.load('images/walk1.png'))
        self.images.append(pygame.image.load('images/walk2.png'))
        self.images.append(pygame.image.load('images/walk3.png'))
        self.images.append(pygame.image.load('images/walk4.png'))
        self.images.append(pygame.image.load('images/walk5.png'))
        self.images.append(pygame.image.load('images/walk6.png'))
        self.images.append(pygame.image.load('images/walk7.png'))
        self.images.append(pygame.image.load('images/walk8.png'))
        self.images.append(pygame.image.load('images/walk9.png'))
        self.images.append(pygame.image.load('images/walk10.png'))

        #index value to get the image from the array
        #initially it is 0 
        self.index = 0

        #now the image that we will display will be the index from the image array 
        self.image = self.images[self.index]

        #creating a rect at position x,y (5,5) of size (150,198) which is the size of sprite 
        self.rect = pygame.Rect(5, 5, 150, 198)
    
    def update(self):
        #when the update method is called, we will increment the index
        self.index += 1

        #if the index is larger than the total images
        if self.index >= len(self.images):
            #we will make the index to 0 again
            self.index = 0
        
        #finally we will update the image that will be displayed
        self.image = self.images[self.index]