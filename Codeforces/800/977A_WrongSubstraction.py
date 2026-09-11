"""
Problem Name: Bear and Big Brother
Problem Code: 791A
Link: https://codeforces.com/problemset/problem/791/A
Rating: 800
Time Complexity: O(log(B/A))
Space Complexity: O(1)

Description:
Determine the number of years it will take for the bear to become larger than his brother.
"""

n, k = map(int, input().split())

for _ in range(k):
    if n % 10 != 0:
        n -= 1
    else:
        n //= 10

print(n)