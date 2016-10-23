#Function to find output limits of geometric transformation
def outputLimits(tforms, xLimitsIn, yLimitsIn):
     u = [xLimitsIn[1], np.mean(xLimitsIn), xLimitsIn[2]]
     v = [yLimitsIn[1], np.mean(yLimitsIn), yLimitsIn[2]]
     
     #Form grid of points
     U,V = np.meshgrid(u,v);
     X,Y = forwardAffineTransform(tforms,U,V);
            
    #XLimitsOut and YLimitsOut from min and max of transformed points.
     xLimitsOut = [min(X), max(X)];
     yLimitsOut = [min(Y), max(Y)];
            
     return xLimitsOut, yLimitsOut
 
#Function to compute forward affine transformation
#Found here: http://stackoverflow.com/questions/37363875/matlab-transformpointsforward-equivalent-in-python 
def forwardAffineTransform(T,v1,v2):
    if v1.shape[1] != 1 or v2.shape[1] != 1:
        print('Vectors must be column-shaped!')
        return
    elif v1.shape[0] != v2.shape[0]:
        print('Vectors must be of equal length!')
        return

    vecSize = v1.shape[0]

    concVec = np.concatenate((v1,v2),axis=1)
    onesVec = np.ones((vecSize,1))

    U = np.concatenate((concVec,onesVec),axis=1)

    retMat = np.dot(U,T[:,0:2])

    return (retMat[:,0].reshape((vecSize,1)), retMat[:,1].reshape((vecSize,1)))