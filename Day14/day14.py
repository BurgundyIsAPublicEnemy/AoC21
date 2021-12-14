from collections import Counter
import time

f = open("Day14.txt", "r")
lines = f.readlines()
state = "HHKONSOSONSVOFCSCNBC"
program_starts = time.time()

for steps in (range(0,39)):
    now = time.time()
    print(steps)

    newState = []

    for char in range(len(state) - 1):
        index = char
        
        nextLetterIndex = index + 1

        foundSomething = False
        for line in lines:
            line = line.replace(" -> ", "|")
            if line.split("|")[0] == (state[index] + state[nextLetterIndex]):
                foundSomething = True
                newState.append(state[index] + line.split("|")[1].strip() + state[nextLetterIndex])
                break
        if (foundSomething == False):
            newState.append(state[index] + state[nextLetterIndex])
        
    state = ""
    for key in range(len(newState)):
        if key != 0:
            state += newState[key][1:]
        else:
            state += newState[key]
    counter = Counter(state)
    print(counter)
    values = sorted(list(counter.values()))

    print((-1 * values[0]) + values[len(values) - 1])
    print("It has been {0} seconds since the loop started".format(now - program_starts))
    

