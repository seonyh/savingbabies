import numpy as np
import cv2
import os
#import PIL

class image_montage(object):
    #load images
    image_list = []
    count = 0;
    for file in os.listdir("test_images"):
        im=cv2.imread(file)
        image_list.append(im)
    
    #read first image from image set    
    I = image_list[0]
    
    #initialize features for first image
    gray_image = I[:][:][1]
    #gray_image = hist_eq(gray_image);
#    points = cv2.cornerHarris(gray_image)