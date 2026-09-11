"""
Problem Name: Sereja & Dima
Problem Code: 381A
Link: https://codeforces.com/problemset/problem/381/A
Rating: 800
Time Complexity: O(N)
Space Complexity: O(1)

Description:
Sereja and Dima are playing a game with a row of cards. Each card has a value, and they take turns picking the card with the highest value from either end of the row. Sereja goes first. The goal is to determine the final scores of both players after all cards have been picked.
"""

n = int(input())
cards = list(map(int, input().split()))

left = 0
right = n - 1

sereja_score = 0
dima_score = 0
turn = 0  # 0 for Sereja, 1 for Dima

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1

    if turn == 0:
        sereja_score += chosen
    else:
        dima_score += chosen

    turn ^= 1  # Alternate turns: 0 -> 1, 1 -> 0

print(sereja_score, dima_score)