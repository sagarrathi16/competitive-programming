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

A, B = map(int, input().split())
years = 0
Bear = A
Big_Brother = B

while Bear <= Big_Brother:
    Bear *= 3
    Big_Brother *= 2
    years += 1

print(years)
        
