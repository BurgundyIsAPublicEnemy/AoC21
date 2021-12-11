f = open("Day9.txt", "r")
lines = f.readlines()

N = 15000
M = 15000

zeros = [ [-1] * N for _ in range(M)]
lowPoints = []

# Create matrix
for r in range(0, len(lines)):
    for c in range (0, len(lines[r].strip())):
        zeros[r][c] = int(lines[r][c].strip())

# Check for low points
for r in range(0, N):
    for c in range (0, M):
        if zeros[r][c] != -1:
            # Get adjacents
            curr = zeros[r][c]

            if ((curr <  zeros[r + 1][c]) or zeros[r + 1][c] == -1):
                if ((curr <  zeros[r - 1][c]) or zeros[r - 1][c] == -1):
                     if ((curr <  zeros[r][c - 1]) or zeros[r][c - 1] == -1):
                          if ((curr <  zeros[r][c + 1]) or zeros[r][c + 1] == -1):
                                 lowPoints.append(curr + 1)
                

print(sum(lowPoints))