import math
import random as rand
import numpy as np
import matplotlib.pyplot as plt

#These constants are to demonstrate the algorithm they can easily be reimplemented to fit the user's needs through input as with the cluster number
NUM_POINTS = 250
NUM_ITERATIONS = 15
X_RANGE = 1000
Y_RANGE = 1000

#Creates random points to use a data set for the k means
def createRandomPoints(numPoints):
    points = []
    for i in range(numPoints):
        x = rand.randint(0, X_RANGE - 1)
        y = rand.randint(0, Y_RANGE - 1)
        point = [x,y]
        points.append(point)
    return points

#Creates randomly placed centers based on user input num
def createRandomCenters(numClusters):
    centers = []
    for i in range(numClusters):
        x = rand.randint(0, X_RANGE - 1)
        y = rand.randint(0, Y_RANGE - 1)
        center = [x,y]
        centers.append(center)
    return centers
        
#Determines the euclidian distance between 2 points
def euclidianDist(pointA, pointB):
        return math.sqrt((pointA[0]-pointB[0])**2 + (pointA[1]-pointB[1])**2)
  
#Assigns each point to the center with shortest euclidian distance between them
def shortestDist(points, centers, minDistIdx):
    for i in range(len(points)):
        for j in range(len(centers)):
            if (i not in minDistIdx or euclidianDist(points[i], centers[j]) < euclidianDist(points[i], centers[minDistIdx[i]])):
                minDistIdx[i] = j

#Move the position of each center to the average of their assigned points
def updateCenters(points, centers, minDistIdx):
    for i in range(len(centers)):
        xSum = 0
        ySum = 0
        counter = 0
        for j in range(len(points)):
            if (minDistIdx[j] == i):
                counter += 1
                xSum += points[j][0]
                ySum += points[j][1]
        if (counter != 0):
            centers[i][0] = int(xSum / counter)
            centers[i][1] = int(ySum / counter)
    
#Creates a dictionary of centers and random colours to use for the plots       
def makeColourPalette(centers):
    colourDict = {}
    for i in range(len(centers)):
        colourDict[i] = "#%06x" % rand.randint(0, 0xffffff)
    return colourDict

#Initializes Components and takes user input for the number of points
minDistIdx = {}
points = createRandomPoints(NUM_POINTS)
k = int(input("How many clusters do you want?"))
centers = createRandomCenters(k)

#Main Loop
for i in range(NUM_ITERATIONS): #Can be changed to stop when the centers stop moving, however a constant amount allows for a simpler implementation
    shortestDist(points, centers, minDistIdx)
    updateCenters(points, centers, minDistIdx)
    
#Plot Results
plt.xlabel('X Values')
plt.ylabel('Y Values')
plt.title('K-Means Clusters')
cv = np.reshape(centers, (k, 2))
colourDict = makeColourPalette(centers)
plt.plot(cv[0:, 0], cv[0:, 1], c='#000000', marker="*", markersize=10, linestyle=None, linewidth=0)
for i in range(len(points)):
    plt.plot(points[i][0], points[i][1], c=colourDict[minDistIdx[i]], marker=".", markersize=8, linestyle=None, linewidth=0)
plt.show()    
