def find_rank(rank, arr):
    if len(arr) == 1:
        return arr[0]

    bigger = list()
    smaller = list()
    pivot = arr.pop()
    for i in arr:
        smaller.append(i) if i < pivot else bigger.append(i)

    if len(smaller) == rank:
        return pivot
    elif len(smaller) > rank:
        return find_rank(rank, smaller)
    else:
        return find_rank(rank - len(smaller) - 1, bigger)


a = [int(i) for i in input().split()]
R = a[0]
C = a[1]
H = a[2]
W = a[3]
mat = [[0] * C for i in range(R)]

for r in range(R):
    a = input().split()
    for c in range(C):
        mat[r][c] = int(a[c])

ans = list()
arr = list()
for r in range(H - 1, R):
    for c in range(W - 1, C):
        arr.clear()
        for item in mat[r - H + 1:r + 1]:
            arr.extend(item[c - W + 1:c + 1])
        ans.append(find_rank(H * W // 2, arr))

print(min(ans))
