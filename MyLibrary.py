#MyLibrary.py 
#Or how to do some modularization
import sys, time, random, math, pygame
from pygame.locals import *

#prints text using the supplied font

def print_text(font, x, y, text, color=(255,255,255)):
    imgText=font.render(text, True, color)
    screen=pygame.display.get_surface()
    screen.blit(imgText,(x,y))