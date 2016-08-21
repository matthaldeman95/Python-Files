from datetime import datetime as dt

def buildaString(str, A, B):
    mint = [n * A for n in range(len(str),0,-1)]
    mint.append(0)
    for n in range(len(str)-1, -1, -1):
        if mint[n+1] + A < mint[n]:
            mint[n] = mint[n + 1] + A
        for m in range(n, 0, -1):
            if B < (n-m+1)*A and B + mint[n+1] < mint[m]:
                if n - m + 1 <= m-1:
                    substr = str[m:n + 1]
                    prestr = str[0:m]
                    if substr in prestr:
                        mint[m] = B + mint[n+1]
                    else:
                        break
                else:
                    break

        """
        if mint[n+1] + A < mint[n]:
            mint[n] = mint[n + 1] + A
        for m in range(n,0,-1):
            substr = str[m:n+1]
            prestr = str[0:m]
            if substr in prestr:
                if(B + mint[n+1]) < mint[m] and B < (len(substr) * A):
                    mint[m] = B + mint[n+1]
            else:
                break
        """
    return mint[0]

A = []
B = []
inputString = []


testcases = raw_input()
for n in range(0,int(testcases)):
    digits = raw_input()
    N, a, b = digits.split(" ")
    A.append(int(a))
    B.append(int(b))
    inputString.append(raw_input())
starttime = dt.now()
for n in range(0,len(A)):
    print buildaString(inputString[n], A[n], B[n])
endtime = dt.now()
dt = (endtime-starttime).total_seconds()
print dt

