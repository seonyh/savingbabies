import numpy as np
import cv2
import os
#import PIL

class image_montage(object):
    
    max_corners = 50
    quality = 0.01
    min_distance = 5
    
    #Load images
    image_list = []
    count = 0;
    im_dir = "test_images"
    for file in os.listdir(im_dir):
        name = im_dir + '/' + file
        im=cv2.imread(name)
        image_list.append(im)
    
    #Read first image from image set    
    I = image_list[0]
    
    #Initialize features for first image
    gray_image = I[:,:,1]
    gray_image = cv2.equalizeHist(gray_image);
    #Detect Harris features. May need to adjust parameters.
    points = cv2.goodFeaturesToTrack(gray_image,max_corners,quality,min_distance,useHarrisDetector = 1)
        #keypoints = cv2.cornerHarris(gray_image,2,3,0.04) 
    
    #Convert points to cv::KeyPoint
    
    freakExtractor = cv2.DescriptorExtractor_create('FREAK')
    points,descriptors = freakExtractor.compute(gray_image,points)