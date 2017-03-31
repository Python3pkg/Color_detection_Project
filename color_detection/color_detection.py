# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 18:30:12 2016

A short software to find the percentage of a range color given
by the user in a natural image and save the resulting image
with the minimum values of the given range

@author: Flavien CHARTON
"""

import os, argparse, glob, sys, datetime
import numpy as np
import cv2

def color_detection(file):
    global filename
    filename = os.path.splitext(os.path.basename(file))[0]
    colorCounter = 0
    image = cv2.imread(file, 1)
    
    # Convert BGR to HSV
    HSVimage = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # define range of color in HSV
    lowerValue = np.array([minHue, 0, 0], dtype = np.uint8)
    upperValue = np.array([maxHue, 255, 255], dtype = np.uint8)

    # Threshold the HSV image to get only the wanted range
    mask = cv2.inRange(HSVimage, lowerValue, upperValue)
    
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if(mask[i, j] == 255):
                colorCounter += 1
                
    colorPercent = (colorCounter * 100) / (float(mask.shape[0]) * float(mask.shape[1]))

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(image, image, mask = mask)

    cv2.imwrite(args['result'] + '/color_detection_' + filename + '.png', result)
    
    print("\nPercentage of pixels in Hue range " + str((minHue, maxHue)) + " for " + filename + " image: " + str(colorPercent) + " %")
    return colorCounter
    
if(__name__ == '__main__'):
    global minHue, maxHue
    print("\nColor detection program for RGB images (dependencies : Python 2.X, OpenCV 2.4.X)")
    
    tries = 0
    while(True):
        dirs = raw_input("Enter a path to the images you want to process (eg. C:/some_image_directory/): ")
        if(os.path.exists(dirs)):
            break
        else:
            print("\nSorry, we failed to find an existing path.\n")
            tries += 1
        if(tries == 3):
            sys.exit()
    tries = 0
    while(True):
        minHue, maxHue = input("Enter a Hue range to find in images you want to process (eg : minHue, maxHue): ")
        if(type(minHue), type(maxHue) == int, int):
            print("\nPlease wait while processing...")            
            break
        else:
            print("\nSorry, wrong variable type, please enter integer variables.\n")
            tries += 1
        if(tries == 3):
            print("\nEnd of tries.\n")
            sys.exit()
    
    resultPath = dirs + str(datetime.date.today()) + "_color_detection_results"
    if not(os.path.exists(dirs + str(datetime.date.today()) + "_color_detection_results")):
        os.makedirs(dirs + str(datetime.date.today()) + "_color_detection_results")
        
    #Build the argument parser and parse the arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', required = True, help = "Path to image files")
    parser.add_argument('--result', required = True, help = "Path to resulting files")
    args = vars(parser.parse_args(['--path', dirs, '--result', resultPath]))
    
    for file in glob.glob(args['path'] + '*'):
        #Check file is a real file and check its extension
        if(os.path.isfile(file) and file.endswith(('.png', '.jpg', '.JPG', '.jpeg'))):
            color_detection(file)
        else:
            continue
        
    print("\nSuccessfully processed.")
