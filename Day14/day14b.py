from collections import defaultdict
state = "HHKONSOSONSVOFCSCNBC"
mappings = {}
for line in open("Day14.txt", "r").readlines():
    mappings[line.strip().split(" -> ")[0]] = line.strip().split(" -> ")[1]
pair_map = defaultdict(int)
for i in range(len(state) - 1):
    pair_map[state[i:i+2]] += 1
for steps in range(40):
    new_pairings, breakDownMapping = defaultdict(int), defaultdict(int)
    for pair in pair_map:
        new_pairings[pair[0] + mappings[pair]] += pair_map[pair]
        new_pairings[mappings[pair] + pair[1]] += pair_map[pair]
    for k, v in new_pairings.items():
        breakDownMapping[k[0]] += v
    breakDownMapping[state[-1]] += 1
    pair_map = new_pairings
print(sorted(list(breakDownMapping.values()))[len(sorted(list(breakDownMapping.values()))) - 1] - sorted(list(breakDownMapping.values()))[0])
