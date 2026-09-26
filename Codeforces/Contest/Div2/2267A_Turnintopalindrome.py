t = int(input())

for i in range(t):
    n, c = input().split()
    n = int(n)

    s = input()

    count = 0

    for j in range(n // 2):
        left = s[j]
        right = s[n - 1 - j]

        if left != right:
            if left == c or right == c:
                count += 1
            else:
                count += 2

    print(count)