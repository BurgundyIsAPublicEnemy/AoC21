import numpy as np 

#setup
with open('Day13A.txt') as f:
    points = [tuple(l.strip().split(',')) for l in f.readlines()]

with open('Day13B.txt') as f:
    folds = [tuple(l.strip().replace("fold along ", "").split('=')) for l in f.readlines()]

paper = np.zeros((2000, 2000))

# i read the file wrong like an idiot and cba to fix it 
transpose = False

#part a is first fold 
for fold in folds:
    firstFold = fold
    lineCoord = int(firstFold[1])
    axis = str(firstFold[0])

    if (not transpose):
        # get inital points
        # if fold on x, get x cord
        # if fold on y , get y cord
        for point in points:
            if axis == 'x':
                paper[int(point[0])][int(point[1])] = int(point[0]) + 1
            if axis == 'y':
                paper[int(point[0])][int(point[1])] = int(point[1]) + 1

        paper = paper.T
        transpose = True
    else: 
        
        for point in points:
            if axis == 'x':
                paper[int(point[1])][int(point[0])] = int(point[0]) + 1
            if axis == 'y':
                paper[int(point[1])][int(point[0])] = int(point[1]) + 1
    
    # get the points we are gonna fold and do some math
    # if fold on y, get their y cord, - the line, and - that again
    # if fold on x , get their x cord, - the line, and - that again
    pointsToFold = np.transpose((paper >= lineCoord).nonzero())

    # get new points
    newPoints = []
    for point in pointsToFold:
        if str(axis) == 'y':
            newPoints.append(tuple([point[1], lineCoord - abs(lineCoord - point[0])]))
        if str(axis) == 'x':
            newPoints.append(tuple([lineCoord - abs(lineCoord - point[1]), point[0]]))
            
    for point in newPoints:
        if axis == 'x':
            paper[int(point[1])][int(point[0])] = int(point[0]) + 1
        if axis == 'y':
            paper[int(point[1])][int(point[0])] = int(point[1]) + 1

    # get slice 
    if str(axis) == 'x':
        paper = paper[:, :lineCoord]
    if str(axis) == 'y':
        paper = paper[:lineCoord , :]
    
    print(len(np.nonzero(paper > 0)[0]))

    vispaper = np.where(paper > 0, 'X', paper) 
    vispaper = np.where(paper == 0, '.', vispaper) 

    # get new ting 
    points = []
    for iy, ix in np.ndindex(vispaper.shape):
        if ((vispaper[iy, ix]) == 'X'):
            points.append(tuple([ix, iy]))

    print("\n")

vispaper = np.where(paper > 0, 'X', paper) 
vispaper = np.where(paper == 0, '.', vispaper) 
print(vispaper)
