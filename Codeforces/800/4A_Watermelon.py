"""
Problem Name: Watermelon
Problem Code: 4A
Link: https://codeforces.com/problemset/problem/4/A
Rating: 800
Time Complexity: O(1)
Space Complexity: O(1)

Description:
Determine if a given weight can be divided into two even parts. 
Any even number can be split into two smaller even numbers, except for 
the number 2, which splits into 1 and 1 (both odd).
"""

w = int(input())

if w%2 == 0 and w > 2:
    print("YES")
else:
    print("NO")
