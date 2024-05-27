
def zeta_transform_2d(a, n):
    #ヨコに累積和
    for i in range(n):
        for j in range(n):
            if i: a[i][j] += a[i-1][j]
    #タテに累積和
    for i in range(n):
        for j in range(n):
            if j: a[i][j] += a[i][j-1]
    return a

def moebius_transform_2d(a, n):
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i: a[i][j] -= a[i-1][j]
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if j: a[i][j] -= a[i][j-1]
    return a

a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = zeta_transform_2d(a, 3)
print(b)
print(moebius_transform_2d(b, 3))