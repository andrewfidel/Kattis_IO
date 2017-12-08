from operator import sub

#  Utilizes List Comprehension
"""
Bijele

User would like to know how many pieces of each type he should add or remove to make a valid set

A valid set contains:
- One King
- One Queen
- Two Rooks
- Two Bishops
- Two Knights
- Eight Pawns

Input1: Kings
Input2: Queens
Input3: Rooks
Input4: Bishops
Input5: Knights
Input6: Pawns

Output: Should consist of 6 integers on a single line, the number of pieces of each type
the user should add or remove
    - If a number is positive, the User needs to add that many pieces, if a number is negative, the User
      needs to remove pieces
    
https://open.kattis.com/problems/bijele
"""
valid_set = [1, 1, 2, 2, 2, 8]
input_set = [0, 1, 2, 2, 2, 7]
input_set2 = [2, 1, 2, 1, 2, 1]

c = map(sub, valid_set, input_set)
print(c)
