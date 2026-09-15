"""
Problem Name: Elephant
Problem Code: 617A
Link: https://codeforces.com/problemset/problem/617/A
Rating: 800
Time Complexity: O(1)
Space Complexity: O(1)

Description:
Determine the number of steps it will take for the elephant to reach the target position. We are given a value of coordiante which is the distination.
We need to find the number of steps it will take for the elephant to reach the target position. The elephant can move a maximum of 5 units in one step. If the distance is greater than 5, it will take multiple steps to reach the target position.
"""

coordinates = int(input())

i = coordinates // 5
if coordinates % 5 != 0:
    i += 1
print(i)
