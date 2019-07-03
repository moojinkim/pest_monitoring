import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plts
import time


def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist

def plot_colors(hist, centroids):
    # initialize the bar chart representing the relative frequency
    # of each of the colors
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    # loop over the percentage of each cluster and the color of
    # each cluster
    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def getColor(data,clusterNum,hlist=[[0,180]],sup=255,sdown=0,vup=255,vdown=0):
    
    # Check the initial time
    start = time.time() 

    # Read the data from the directory named data.
    src = cv2.imread(data, cv2.IMREAD_COLOR)

    # Convert the image to hsv format.
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv)

    # Mask the image by hsv input condition
    # v and s has one interval 
    # h has sevral interval and it returns the union of the interval. 
    mask = cv2.inRange(v,vdown,vup)
    mask2 = cv2.inRange(s,sdown,sup)
    mask3 = cv2.inRange(h,0,180)
    for i in hlist:
        mask3 = mask3 + cv2.inRange(h,i[0],i[1])
    
    res = cv2.bitwise_and(src, src, mask=mask)
    res = cv2.bitwise_and(res, res, mask=mask2)
    bgr = cv2.bitwise_and(res, res, mask=mask3)

    # openCV get a image as a BGR format
    # Convert the image to RGB format
    rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)

    # Reshape for applying Kmean function to the image.
    rgb = rgb.reshape(rgb.shape[0] * rgb.shape[1], 3)

    # The masked area has (0,0,0) RGB value
    blackPoint= np.array([0,0,0])
    k=0
    bdelete = []
    for i in rgb:
        if np.array_equal(i,blackPoint):

            # Find the Black point and append in bdelete list
            bdelete.append(k)
        k=k+1

    #Delete the Masked area from the image.
    rgb2=np.delete(rgb, bdelete,0)

    # The number of cluster is 5
    clusterNum = 5 

    # Calculate the Color Clusters of Image by the KMeans Class.
    clt = KMeans(n_clusters = clusterNum)
    clt.fit(rgb2)

    #Represent the time to finish the clustering
    print("time - clustering is finished :", time.time() - start)
    centers = []


    # # show our color bart
    # hist = centroid_histogram(clt)
    # bar = plot_colors(hist, clt.cluster_centers_)
    
    # plts.figure()
    # plts.axis("off")
    # plts.imshow(bar)
    # plts.show()

    return(clt.cluster_centers_)





