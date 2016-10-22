import numpy as np
import cv2
import os

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
    surf = cv2.SURF();
    #harrisDetector = cv2.FeatureDetector_create('HARRIS')
    freakExtractor = cv2.DescriptorExtractor_create('FREAK')
    keypoints = surf.detect(gray_image)
    print 3
    (points, descriptors) = freakExtractor.compute(gray_image,keypoints)
    print 4

    #Initialize transforms to identity matrix
    tforms = [np.identity(3) for i in range(len(image_list))]

    #Iterate over remaining image pairs
    for index in range(1,len(image_list)):
        print 5
        points_previous = points;
        descriptors_previous = descriptors;
        I = image_list[index]
        gray_image = I[:,:,1]
        gray_image = cv2.equalizeHist(gray_image)
        
        #Detect Harris features. May need to adjust parameters.
        surf = cv2.SURF();
        #harrisDetector = cv2.FeatureDetector_create('HARRIS')
        freakExtractor = cv2.DescriptorExtractor_create('FREAK')
        keypoints = surf.detect(gray_image)
        (points, descriptors) = freakExtractor.compute(gray_image,keypoints)

        #Match descriptors
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(descriptors,descriptors_previous)
        #These two lines are probably definitely wrong:
        #matchedPoints = matches[2:3, :];
        #matchedPointsPrev = matches[0:1, :];
        
        #tforms[n] = getPerspectiveTransform(matchedPoints, matchedPointsPrev)
        #tforms[n] = tforms[n-1] * tforms[n]
    print 6
   
 #  for index in range(len(tforms)):
  #     [xlim[i,:], ylim[i,:]] = outputLimits(tforms(i), [1 imageSize(2)], [1 imageSize(1)]) 

    
        