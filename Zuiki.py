#
# ZUKI MasCon input converter for Densha de Go!! AC 2017
#
# version 1.3.1
# 
# This script maps movements of ZUKI Master Controller to up and down mouse wheel movement events
# allowing accelaration and breaking control in Densha de Go!! AC 2017 (tested with version 5.80.02)
# running natively on Windows, without Teknoparrot emulation and key mappings
# 
# Due to pygame compatibility problems with newer versions of Python (as of late December 2025)
# Python 3.13 is the highest recommended version
#   
# Tested with pygame 2.6.1 (SDL 2.28.4, Python 3.13.11) and pydirectinput-rgx 2.1.3
# (standard pydirectinput does not support mouse scroll functionality)
# https://pypi.org/project/pydirectinput-rgx/
#

import pydirectinput 
import pygame

# Lowest possible delay before the game starts dropping key presses
INPUT_PAUSE = 0.07

pydirectinput.PAUSE = INPUT_PAUSE  
pygame.init()
clock = pygame.time.Clock()

# Controller detection
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
joystick_list = []

for i in range(pygame.joystick.get_count()):
    jid = {'joyid': i, 'joyname': pygame.joystick.Joystick(i).get_name()}
    joystick_list.append(jid)
    print()
    print("List of detected joystick(s):")
    for i, item in enumerate(joystick_list):
        print(item)
    print()

mascon_select = None
for i, item in enumerate(joystick_list):
    if item["joyname"] in {"ZUIKI MasCon for Nintendo Switch",
                           "One Handle MasCon for Nintendo Switch",
                           "One Handle MasCon for Nintendo Switch Exclusive Edition"}:
        mascon_select = i

if mascon_select is None:
    print()
    print('#####################################################################################')
    print('#  No MasCon found.                                                                 #')
    print('#  Connect the correct controller and restart the script.                           #')
    print('#  Press <Enter> to exit.                                                           #')
    print('#####################################################################################')
    print()
    input()
    exit()

print('#####################################################################################')
print('#  Remember to start the game with the MasCon in neutral (N) position.              #')
print('#  Press CTRL + C to exit.                                                          #')
print('#####################################################################################')
print()

mascon_mapping = {
   1.00: [ 15, "P5" ],
   0.80: [ 14, "P4" ],
   0.61: [ 13, "P3" ],
   0.43: [ 12, "P2" ],
   0.24: [ 11, "P1" ],
   0.00: [ 10, "N" ],
   -0.21: [ 9, "B1" ],
   -0.32: [ 8, "B2" ],
   -0.43: [ 7, "B3" ],
   -0.53: [ 6, "B4" ],
   -0.64: [ 5, "B5" ],
   -0.75: [ 4, "B6" ],
   -0.85: [ 3, "B7" ],
   -0.96: [ 2, "B8" ],
   -1.00: [ 1, "EB" ]
}

# Detect initial lever position
mascon_axis = (round(joysticks[mascon_select].get_axis(1), 2)) 
mascon_pos = mascon_mapping[mascon_axis][0]
mascon_pos_old = mascon_pos

def handle_mascon_pos():
    if mascon_pos>mascon_pos_old:
        print("DOWN")
        pydirectinput.scroll(-1)      
    if mascon_pos<mascon_pos_old:
        print("UP")
        pydirectinput.scroll(1)
    print()

pygame.event.clear()

while 1:
    for event in pygame.event.get():
        print (event)
        if event.type == pygame.JOYAXISMOTION:
            mascon_axis = (round(event.value, 2))    
            print(mascon_axis)
            print(mascon_mapping[mascon_axis][1])
            mascon_pos_old = mascon_pos
            mascon_pos = mascon_mapping[mascon_axis][0]
            handle_mascon_pos()

        if (event.type == pygame.JOYBUTTONDOWN): 
            if event.button == 2: 
                print ("HORN ON")
                pydirectinput.keyDown('space')

        if (event.type == pygame.JOYBUTTONUP): 
            if event.button == 2: 
                print ("HORN OFF")
                pydirectinput.keyUp('space')                
    
    clock.tick_busy_loop(60)