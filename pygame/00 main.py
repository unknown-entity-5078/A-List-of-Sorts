import pygame
import os
import time

from bubblesort import *
from quicksort import *
from mergesort import *

# Initialization
pygame.init()
pygame.font.init()
window_size = (1000, 700)
window = pygame.display.set_mode((window_size))
pygame.display.set_caption("A list of Sort")

def update_draw():
    pygame.display.flip()
    pygame.display.update()
    pygame.time.Clock().tick(1000000000)

def buffer():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

# Colour sets
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
background_colour = pygame.Color(245, 138, 7)
config_colour = pygame.Color(67, 67, 67)
title_colour = pygame.Color(40, 40, 40)

# Font set
title_font = pygame.font.SysFont('Helvetica Neue Bold', 85)
config_font = pygame.font.SysFont('Helvetica Neue Bold', 50)

# Top title bar
title_height = 70
spacing = 30

def setTitle():
    window.fill(background_colour)
    title_text = title_font.render('Sorting', True, title_colour)
    window.blit(title_text,(spacing,5))
    pygame.draw.rect(window, title_colour, (spacing, title_height, window_size[0]-(2*spacing), 2), 0)
    update_draw()

# The 4 sorting boxes
sortingBoxes_size_w, sortingBoxes_size_h = (window_size[0]-(3*spacing))/2, (window_size[1]-title_height-(3*spacing))/2

bubblesort_frame = (spacing, title_height+spacing)
quicksort_frame = (window_size[0]-spacing-sortingBoxes_size_w, title_height+spacing)
mergesort_frame = (spacing, window_size[1]-spacing-sortingBoxes_size_h)
insertionsort_frame = (window_size[0]-spacing-sortingBoxes_size_w, window_size[1]-spacing-sortingBoxes_size_h)

bubblesort_btn = pygame.image.load('bubblesort_btn.png')
quicksort_btn = pygame.image.load('quicksort_btn.png')
mergesort_btn = pygame.image.load('mergesort_btn.png')
insertionsort_btn = pygame.image.load('insertionsort_btn.png')

def setBoxes():
    window.blit(bubblesort_btn, bubblesort_frame)
    window.blit(quicksort_btn, quicksort_frame)
    window.blit(mergesort_btn, mergesort_frame)
    window.blit(insertionsort_btn, insertionsort_frame)

    update_draw()

setTitle()
setBoxes()

# Clicking action
# Config button
bubblesortConfig_btn = pygame.image.load('bubblesortConfig_btn.png')
quicksortConfig_btn = pygame.image.load('quicksortConfig_btn.png')
mergesortConfig_btn = pygame.image.load('mergesortConfig_btn.png')
insertionsortConfig_btn = pygame.image.load('insertionsortConfig_btn.png')

stepper_btn = pygame.image.load('stepper_btn.png')

# Run button
run_btn = pygame.image.load('run_btn.png')

# Sorting config
runBtn_x, runBtn_y, runBtn_w, runBtn_h = 324, 200, 116, 56
speedText_x, speedText_y, speedText_w, speedText_h = 216, 89, 45, 39 
listlengthText_x, listlengthText_y, listlengthText_w, listlengthText_h = 216, 145, 37, 39 
speed = float(1.0)
listlength = 10
stepper_x = 90

def showConfig(frame, show_image):
    # Show image
    window.blit(show_image, frame)
    # Show config
    speedConfig_text = config_font.render(str(round(speed,1)) + ' x', True, config_colour)
    listlengthConfig_text = config_font.render(str(listlength), True, config_colour)
    window.blit(speedConfig_text,(frame[0]+speedText_x, frame[1]+speedText_y))
    window.blit(listlengthConfig_text,(frame[0]+listlengthText_x, frame[1]+listlengthText_y))

    window.blit(stepper_btn,(frame[0]+speedText_x+stepper_x, frame[1]+speedText_y-3))
    window.blit(stepper_btn,(frame[0]+listlengthText_x+stepper_x, frame[1]+listlengthText_y-3))
    update_draw()

# Check if cursor in box
def cursor(frame, sort_image, show_image):
    global speed, listlength

    mouse_pos = pygame.mouse.get_pos()
    if frame[0]+sortingBoxes_size_w > mouse_pos[0] > frame[0] and frame[1]+sortingBoxes_size_h > mouse_pos[1] > frame[1]:
        showConfig(frame, show_image)

        # Mouse click in stepper
        if event.type == pygame.MOUSEBUTTONDOWN: 
            # Stepper for speed
            # - 
            if 0.2 < speed: 
                if frame[0]+speedText_x+stepper_x+50 > mouse_pos[0] > frame[0]+speedText_x+stepper_x and frame[1]+speedText_y-3+39 > mouse_pos[1] > frame[1]+speedText_y-3:
                    speed -= 0.1
                    showConfig(frame, show_image)
            # + 
            if speed < 4.9:  
                if frame[0]+speedText_x+stepper_x+100 > mouse_pos[0] > frame[0]+speedText_x+stepper_x+50 and frame[1]+speedText_y-3+39 > mouse_pos[1] > frame[1]+speedText_y-3:         
                    speed += 0.1
                    showConfig(frame, show_image)
            
            # Stepper for listlength
            # -
            if 1 < listlength:  
                if frame[0]+listlengthText_x+stepper_x+50 > mouse_pos[0] > frame[0]+listlengthText_x+stepper_x and frame[1]+listlengthText_y-3+39 > mouse_pos[1] > frame[1]+listlengthText_y-3:
                    listlength -= 1
                    showConfig(frame, show_image)
            # +
            if listlength < 100: 
                if frame[0]+listlengthText_x+stepper_x+100 > mouse_pos[0] > frame[0]+listlengthText_x+stepper_x+50 and frame[1]+listlengthText_y-3+39 > mouse_pos[1] > frame[1]+listlengthText_y-3:
                    listlength += 1
                    showConfig(frame, show_image)

        # Mouse click in box
        if frame[0]+runBtn_x+runBtn_w > mouse_pos[0] > frame[0]+runBtn_x and frame[1]+runBtn_y+runBtn_h > mouse_pos[1] > frame[1]+runBtn_y:
            window.blit(run_btn, (frame[0]+runBtn_x, frame[1]+runBtn_y))
            update_draw()
            if event.type == pygame.MOUSEBUTTONDOWN: return True
        
    else:
        window.blit(sort_image, frame)
        update_draw()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if cursor(bubblesort_frame, bubblesort_btn, bubblesortConfig_btn):
            bubblesort(speed, listlength)
            setTitle() # Reset
            setBoxes()
        elif cursor(quicksort_frame, quicksort_btn, quicksortConfig_btn):
            quicksort(speed, listlength)
            setTitle() # Reset
            setBoxes()
        elif cursor(mergesort_frame, mergesort_btn, mergesortConfig_btn):
            mergesort(speed, listlength)
            setTitle() # Reset
            setBoxes()
        elif cursor(insertionsort_frame, insertionsort_btn, insertionsortConfig_btn): # Algorithm not done
            # insertionsort()
            setTitle() # Reset
            setBoxes()










'''
        # Cursor in bubblesort
        bubblesortChange = False
        if bubblesort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > bubblesort_frame[0] and bubblesort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > bubblesort_frame[1]:
            bubblesortChange= True
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if bubblesort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > bubblesort_frame[0] and bubblesort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > bubblesort_frame[1]:
                    run_btn.set_alpha(i)
                    window.blit(run_btn, bubblesort_frame)
                    update_draw()
                    buffer()
                else: break
        if bubblesortChange:
            bubblesortChange = False
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if bubblesort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > bubblesort_frame[0] and bubblesort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > bubblesort_frame[1]:
                    break
                else:
                    bubblesort_btn.set_alpha(i)
                    window.blit(bubblesort_btn, bubblesort_frame)
                    update_draw()
                    buffer()

        # Cursor in quicksort
        if quicksort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > quicksort_frame[0] and quicksort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > quicksort_frame[1]:
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if quicksort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > quicksort_frame[0] and quicksort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > quicksort_frame[1]:
                    run_btn.set_alpha(i)
                    window.blit(run_btn, quicksort_frame)
                    update_draw()
                    buffer()
                else: break
        else:
            for i in range(100, 256, 15):
                mouse_pos = pygame.mouse.get_pos()
                if quicksort_frame[0]+sortingBoxes_size_w > mouse_pos[0] > quicksort_frame[0] and quicksort_frame[1]+sortingBoxes_size_h > mouse_pos[1] > quicksort_frame[1]:
                    break
                else:
                    quicksort_btn.set_alpha(i)
                    window.blit(quicksort_btn, quicksort_frame)
                    update_draw()
                    buffer()
'''
