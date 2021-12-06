import numpy as np
import pandas as pd
f = open("Day4.txt", "r")
lines = f.readlines()

tmpinu = ""
allRows = []
tmp = []
for x in range(0, len(lines)):
    # line 1 is input
    
    if (x == 0):
        tmpinu = lines[x].split(',')
    
    else:
        #convert into matrix
        if lines[x].strip():
            tmp.append(np.array(lines[x].split()))
        else:
            if (tmp):
                allRows.append(pd.DataFrame(tmp))
                tmp = []

allRows.append(pd.DataFrame(tmp))

steps = 0
fastest = 100
did = 0
winner = 0
d_id_tmp = 0

scores = []
scoreSteps = []

for df in allRows:
    steps = 0
    tmpDF = df
    for i in tmpinu:

        tmpDF = tmpDF.replace(i, "X")
        t_columns = tmpDF.columns[tmpDF.nunique() <= 1].values

        if t_columns.size != 0:
            if (fastest > steps):
                fastest = steps
                did = d_id_tmp
                winner = i
                scores.append(steps)
                scoreSteps.append(i)
                break

        tmpDF2 = tmpDF.T
        t_rows = tmpDF2.columns[tmpDF2.nunique() <= 1].values

        if t_rows.size != 0:
            if (fastest > steps):
                fastest = steps
                did = d_id_tmp
                winner = i
                scores.append(steps)
                scoreSteps.append(i)
                break

        steps += 1
    d_id_tmp += 1
    fastest = 100


did = scores.index(max(scores))
fastest = (max(scores))

winner = int(scoreSteps[did])

print(fastest, did)

finalDF = allRows[did]
tmpDF = finalDF

replaysteps = 0
for i in tmpinu:
    if (replaysteps > fastest):
        break
    tmpDF = tmpDF.replace(i, 0)
    replaysteps += 1

for c in tmpDF.columns:
    tmpDF[c] = pd.to_numeric(tmpDF[c], errors='coerce')

print(did, fastest, winner)

x = (tmpDF.sum(numeric_only=True).sum())

print(int(winner) * int(x))

