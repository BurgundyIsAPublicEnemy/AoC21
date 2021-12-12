import networkx as nx

# HELP REQUIRED!
# Was running out of time cause Christmas shopping

#setup
with open('Day12.txt') as f:
    G = nx.Graph([tuple(l.strip().split('-')) for l in f.readlines()])

#part a
def parta(node, visited):
    sum = 0
    v = visited.copy()

    if node == 'end':
        return 1
    if node in visited:
        return 0
    if node.islower():
        v.append(node)

    for child in G[node]:
        sum += parta(child, v)
    return sum

#part b
def partb(node, visited, visitedBefore):
    sum = 0
    v = visited.copy()

    if node == 'end':
        return 1
    if node in visited:
        if visitedBefore:
            return 0
        else:
            if node == 'start':
                return 0
            visitedBefore = True
    if node.islower():
        v.append(node)

    for child in G[node]:
        sum += partb(child, v, visitedBefore)
    return sum


print(parta("start", []))
print(partb("start", [], False))