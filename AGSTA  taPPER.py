import time
import pygame
from pygame.locals import *
c=0
starttime=time.time()
endtime=time.time()+30.0
pygame.init()
pygame.display.set_mode((800,1000))
pygame.display.set_caption('TAP IF U CAN')
running = True
print(starttime)
while running:
   for event in pygame.event.get():
       if(time.time()<=endtime):
           if ((event.type == MOUSEBUTTONDOWN)):
             c+=1
             print("FASTER!*!*!") 
       else:
           running=False
           break
pygame.display.quit()
if (150>c>50):
    print("OKAY TAPPER U HAVE TAPPED",c,"times in  30 seconds")
elif(300>c>150):
    print("U R a exotic tapper u have TAPPED",c,"times in 30 seconds")
elif (c>350):
    print("U R a LEGENDARY TAPPER u have TAPPED",c,"times in 30 seconds")
else:
    print("GET LOSTT U R UNFIT TO BE A HUMAN BEINNGG!!!!!")
    
