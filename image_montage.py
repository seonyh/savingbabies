#NOTE: Line 69 on needs debugging

import numpy as np
import cv2
import os
import additional_fcns as af

class image_montage(object):
    
    #pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
    #pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    #M = cv2.getPerspectiveTransform(pts1,pts2)
    
    max_corners = 50
    quality = 0.1
    min_distance = 5
    Hessian = 6000;
    
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

    #Detect SURF features. May need to adjust parameters.
    surf = cv2.SURF(Hessian);
    #harrisDetector = cv2.FeatureDetector_create('HARRIS')
    freakExtractor = cv2.DescriptorExtractor_create('FREAK')
    pts = surf.detect(gray_image)
    (pts, des) = freakExtractor.compute(gray_image,pts)

    #Initialize transforms to identity matrix
    tforms = [np.identity(3) for i in range(len(image_list))]

    #Iterate over remaining image pairs
    for index in range(1,len(image_list)):
        pts_old = pts;
        des_old = des;
        I = image_list[index]
        gray_image = I[:,:,1]
        gray_image = cv2.equalizeHist(gray_image)

        #Detect SURF features
        surf = cv2.SURF(Hessian);
        #harrisDetector = cv2.FeatureDetector_create('HARRIS')
        freakExtractor = cv2.DescriptorExtractor_create('FREAK')
        pts = surf.detect(gray_image) 
        (pts, des) = freakExtractor.compute(gray_image,pts)

        #Match descriptors
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
        matches = bf.knnMatch(des,des_old, k=2)
        #matches = sorted(matches, key = lambda x:x.distance)

        pt1 = []        
        pts2 = []
        
        #Based on page 184: https://media.readthedocs.org/pdf/opencv-python-tutroals/latest/opencv-python-tutroals.pdf
        # Ratio test from Lowe's paper
        for m in matches:
            if len(m) == 2 and m[0].distance < m[1].distance * 0.75:
                m = m[0]
                pts2.append(pts[m.trainIdx])
                pts1.append(pt2_old[m.queryIdx])
                
        pts1 = np.float32([kp.pt for kp in pts1])
        pts2 = np.float32([kp.pt for kp in pts2])

        tforms[index] = cv2.getPerspectiveTransform(pts2, pts2)
       
        tforms[n] = tforms[n-1] * tforms[n]
        
    im_size = size(I)

    for i in range(len(tforms)):
        xlim[i,:], ylim[i,:] = af.outputLimits(tforms[i], [1,im_size[1]], [1,im_size[2]])
    
        