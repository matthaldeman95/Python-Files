
def rotate(array, rotations):
    return array[len(array)-rotations:] + array[:len(array)-rotations]

line = raw_input()
n, k, q = line.split(" ")
n, k, q = int(n), int(k), int(q)

numline = raw_input()
arr = numline.split(' ')
arr = rotate(arr,k%len(arr))

queries = []
for y in range(q):
    queries.append(arr[input()])

for z in range(q):
    print queries[z]





