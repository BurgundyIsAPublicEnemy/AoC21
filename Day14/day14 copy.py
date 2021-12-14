import time
from threading import Thread
import threading
import sys
import random
import re
import collections

state = "NBCCNBBBCBHCB"
polymers = {}
k = False

class M(threading.Thread):
    def __init__(self, key, value):
        super(M, self).__init__()
        self.key = key
        self.value = value

    def run(self):
        global state, polymers
        for n in [m.start() for m in re.finditer(self.key, state)]:
            polymers[n] = (self.key[0] + self.value.strip() + self.key[1])
        

f = open("Day14.txt", "r")
lines = f.readlines()

swaps = {}
for line in lines:
    line = line.replace(" -> ", "|")
    if line.split("|")[0] in state:
        swaps[line.split("|")[0]] = line.split("|")[1].strip()

print(swaps)
jobs = []
for key in swaps:
    t = M(key, swaps[key])
    jobs.append(t)

for j in jobs:
    j.start()

# Ensure all of the threads have finished
for j in jobs:
    j.join()

polymers = collections.OrderedDict(sorted(polymers.items()))
state = ""
for key in polymers:
    if key != 0:
        state += polymers[key][1:]
    else:
        state = polymers[key]

print(state)

print(len(state))
print(len("NBBBCNCCNBBNBNBBCHBHHBCHB"))

print (state == "NBBBCNCCNBBNBNBBCHBHHBCHB")