t = int(input())

for i in range(t):
    n, k = map(int, input().split())

    print((k-1)*2 + 2**(n-k+1))