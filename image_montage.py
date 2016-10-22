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
        
        #Detect SURF features
        surf = cv2.SURF();
        #harrisDetector = cv2.FeatureDetector_create('HARRIS')
        freakExtractor = cv2.DescriptorExtractor_create('FREAK')
        keypoints = surf.detect(gray_image)
        (points, descriptors) = freakExtractor.compute(gray_image,keypoints)

        #Match descriptors
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(descriptors,descriptors_previous)
        matches = sorted(matches, key = lambda x:x.distance)
        matchedPointsPrev = []
        matchedPoints = []
        
        #Based on page 184: https://media.readthedocs.org/pdf/opencv-python-tutroals/latest/opencv-python-tutroals.pdf
        matchedPointsPrev.append(points_previous[matches[i in range(len(matches))].trainIdx])
        matchedPoints.append(points[matches[i in range(len(matches))].queryIdx])
        matchedPointsPrev = np.asarray(matchedPointsPrev)
        matchedPoints = np.asarray(matchedPoints)
        
        print type(matchedPoints)
        
        # Apply ratio test to determine good points
        #good_matches = []
        #for i in range(len(matches)):
        #    if m.distance < 0.75*n.distance:
        #        good_matches.append([m])
        
        tforms[index] = cv2.getPerspectiveTransform(matchedPointsPrev, matchedPoints)
        #tforms[n] = tforms[n-1] * tforms[n]
    print 6

        