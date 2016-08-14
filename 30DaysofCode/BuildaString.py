

def buildaString(inString, A, B):
    outString = ""
    cost = 0
    letter = 0
    while letter <= len(inString)-1:
        foundin = False
        for rightind in range(len(inString), letter+1, -1):
            subString = inString[letter:rightind]
            if subString in outString and B < (A*len(subString)):
                outString += subString
                cost += B
                foundin = True
                letter += len(subString)
                break
        if not foundin:
            outString += inString[letter]
            cost += A
            letter += 1
    return cost

A = []
B = []
inputString = []


testcases = raw_input("Enter number of test cases:  ")
for n in range(0,int(testcases)):
    digits = raw_input("Enter length of string, cost A, and cost B, "
                       "separated by spaces:  ")
    N, a, b = digits.split(" ")
    A.append(int(a))
    B.append(int(b))
    inputString.append(raw_input("Type the string to build:  "))

for n in range(0,len(A)):
    print buildaString(inputString[n], A[n], B[n])


