
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


#注意：あらかじめ素数のリスト primes を作成する
def zeta_divisor(a,primes): #aを約数ゼータ
    n = len(a)-1
    for p in primes:
        for i in range(n//p,0,-1):
            a[i] += a[p*i]
    return a

def mobius_divisor(a,primes): #aを約数メビウス
    n = len(a)
    for p in primes:
        for i in range(1,n):
            if i*p >= n: break
            a[i] -= a[p*i]
    return a


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = zeta_transform_2d(a, 3)
print(b)
print(moebius_transform_2d(b, 3))


a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = [2, 3, 5, 7, 11]
b = zeta_divisor(a, primes)
print(b)
print(mobius_divisor(b, primes))
