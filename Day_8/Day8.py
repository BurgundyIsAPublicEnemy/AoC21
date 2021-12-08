import itertools

# SHOUT OUT TO https://github.com/julian-west/adventofcode/blob/master/2021/day_08/d8_solution.py for the help!
# Attempt 1: Get lengths (easy enough), felt I was gonna permuate cause it was only 7! / (7 - 7)! = 5040 but code became spagetthi and logic was rough
# What did I learn? List Comprehension, For Each

f = open("Day8.txt", "r")
lines = f.readlines()

# We sort the mappings so they line up nicely.
initialMapping = {'0': 'abcefg', '1': 'cf', '2': 'acdeg', '3': 'acdfg', '4': 'bcdf',
    '5': 'abdfg', '6': 'abdefg', '7': 'acf', '8': 'abcdefg', '9': 'abcdfg'}

# This inverses the map
initialKV = {v: k for k, v in initialMapping.items()}
dist = 'abcdefg'

total = 0
for line in lines:
    first = line.strip().split('|')[0].strip().split()
    second = line.strip().split('|')[1].strip().split()
    mapping = ""

    for perms in itertools.permutations(dist):

        # the mapping gets set here
        mapping = dict(zip(perms, list(dist)))

        for letters in first:
            # LIST COMPREHENSION
            # [ expression for item in list ]
            # basically... we get the input sentence... get each word
            # then run the word through the permeated mapping 
            # and sort it
            tmp = ''.join(sorted(mapping[c] for c in letters))
        
            print (first, " ; ", letters)

            # if the mapping cannot be found, break out, and try again with a new perm
            if not tmp in initialMapping.values():
                break
        # FOR ELSE
        # Once loop ends.. do this 
        else:
            break

    # Now we have the mapping that matches input
    # Executed outside then in
    # Get word from output sentence
    # Get Letter from Output sentence
    # check the mapping against
    # Sort it and check against the inversed map to give us back a number
    total += int(''.join(initialKV[''.join(sorted(mapping[c] for c in o))] for o in second))
    
print(total)
