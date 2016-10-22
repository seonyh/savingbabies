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
    harrisDetector = cv2.FeatureDetector_create("HARRIS")
    freakDescriptorExtractor = cv2.DescriptorExtractor_create("FREAK")
    keypoints = harrisDetector.detect(gray_image)
    (keypoints, descriptors) = freakDescriptorExtractor.compute(gray_image,keypoints)
    
    #Initialize transforms to identity matrix
    tforms = [cv2.warpPerspective(np.identity(3)) for i in range(len(image_list))]

    #Iterate over remaining image pairs
    for index in range(1,len(image_list)):
        keypoints_previous = keypoints;
        descriptors_previous = descriptors;
        I = image_list[index]
        gray_image = I[:,:,1]
        gray_image = cv.equalizeHist(gray_image)
        
        #Detect Harris features. May need to adjust parameters.
        harrisDetector = cv2.FeatureDetector_create("HARRIS")
        freakDescriptorExtractor = cv2.DescriptorExtractor_create("FREAK")
        keypoints = harrisDetector.detect(gray_image)
        (keypoints, descriptors) = freakDescriptorExtractor.compute(gray_image,keypoints)
        
    
    