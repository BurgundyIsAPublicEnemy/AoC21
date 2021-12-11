def checkBrackets(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "[", "<"]:
             stack.append(char)
        else:

            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '<':
                if char != ">":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # if stack is empty... it's incomplete
    if stack:
        return stack
    return True
 
 
# Driver Code
if __name__ == "__main__":
    points = []
    f = open("Day10.txt", "r")
    lines = f.readlines()
    lineInd = 0
    mappingPoints = {"(" : 1, "[" : 2, "{" : 3, "<" : 4}

    for expr in lines:
        tmpPoints = 0
        m = checkBrackets(expr.strip())
        if (m != False):
            for x in m[::-1]:
                tmpPoints = tmpPoints * 5
                tmpPoints += mappingPoints[str(x)]
                
            points.append(tmpPoints)
        tmpPoints = 0
        lineInd += 1

points = ((sorted(points)))
print(int((len(points) - 1)/2))
print(points[int ((len(points) - 1)/2) ])