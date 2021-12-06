import sys

f = open("puzzleinputs/Day1.txt","r")
lines = f.readlines()

increaseCount = 0
current = 0
index = 0


## PART 1
for line in lines:
    if index == 0: 
        current = int(line)
        print('N/A - no previous measurement)')
    else:
        if (current < int(line)):
            print("Increased")
            current = int(line)
            increaseCount += 1 
        elif (current > int(line)):
            print("Decreased")
            current = int(line)
        else:
            print('N/A - no previous measurement)')
    index += 1


print(increaseCount)



## PART 2

rollingIndex = 0
index = 0
currentRollingSum = [0, 0, 0]
increaseCount = 0
current = 0
signal = 0
for index in range(0, len(lines)):
    for subindex in range(0, len(lines)):

        if (signal == 1):
            print(increaseCount)
            sys.exit(0)

        if (rollingIndex == 3):

            if index != 0:

                if (sum(currentRollingSum) == current):
                    current = sum(currentRollingSum)
                    print(sum(currentRollingSum), "- (N/A - no previous sum)")
                    current = sum(currentRollingSum)
                
                elif (sum(currentRollingSum) > current):
                    current = sum(currentRollingSum)
                    print(sum(currentRollingSum), "- increased")
                    increaseCount += 1
                
                elif (sum(currentRollingSum) < current):
                    current = sum(currentRollingSum)
                    print(sum(currentRollingSum), "- decreased")
            else: 
                print(sum(currentRollingSum), "- (N/A - no previous sum)")
                current = sum(currentRollingSum)

            rollingIndex = 0

            
            break
        

        # Load up the first sweep
        if index == 0:
            currentRollingSum[rollingIndex] = int(lines[index + subindex])        
            rollingIndex += 1
        else: 
            try: 
                currentRollingSum[rollingIndex] = int(lines[index + subindex]) 
            except: 
                #Signal game over
                signal = 1
            rollingIndex += 1
        
    index += 1

    


