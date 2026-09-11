"""
Problem Name: Team
Problem Code: 231A
Link: https://codeforces.com/problemset/problem/231/A
Rating: 800
Time Complexity: O(N)
Space Complexity: O(1)

Description:
Determine the number of problems that can be solved by the team
Given the number of problems each member can solve, determine how many problems the team can solve together.
"""

n =int(input())
solved = 0

for _ in range(n):
    p,v,t = map(int,input().split())

    if p == 1 and v == 1:
        solved += 1
    elif p == 1 and t == 1:
        solved += 1
    elif v == 1 and t == 1:
        solved += 1

print(solved)

    
