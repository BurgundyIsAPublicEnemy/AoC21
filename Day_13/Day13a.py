import numpy as np 

#setup
with open('Day13A.txt') as f:
    points = [tuple(l.strip().split(',')) for l in f.readlines()]

with open('Day13B.txt') as f:
    folds = [tuple(l.strip().replace("fold along ", "").split('=')) for l in f.readlines()]

paper = np.zeros((2000, 2000))

#part a is first fold 
for fold in folds:
    firstFold = fold
    lineCoord = int(firstFold[1])
    for point in points:
        if str(firstFold[0]) == 'x':
            paper[int(point[0])][int(point[1])] = int(point[0]) + 1
        if str(firstFold[0]) == 'y':
            paper[int(point[0])][int(point[1])] = int(point[1]) + 1

    pointsToFold = np.transpose((paper > lineCoord).nonzero())
    newFoldedPaper = paper.copy()

    newPoints = []
    for point in pointsToFold:
        newPoints.append(tuple([point[0], lineCoord - abs(lineCoord - point[1])]))

    for point in newPoints:
        if str(firstFold[0]) == 'x':
            paper[int(point[0])][int(point[1])] = int(point[0])
        if str(firstFold[0]) == 'y':
            paper[int(point[0])][int(point[1])] = int(point[0])
    # slice paper 
    if str(firstFold[0]) == 'x':
        paper = paper[:, :lineCoord]
    if str(firstFold[0]) == 'y':
        paper = paper[:lineCoord , :]
    points = np.argwhere(paper > 0)
    print(paper)
    print(len(np.nonzero(paper > 0)[0]))