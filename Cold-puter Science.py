"""
Cold-puter Science

First line input: single positive integer that specifies the number of temperatures collected
Second line input: contains n temperatures, each separated by a space
    - Each temperature is represented by an integer t

Output: a single integer: the number of temperatures strictly less than zero

https://open.kattis.com/problems/cold
"""

count = 3
list_temps = [5, -10, 15]
list2_temps = [-14, -5, -39, -5, -7]
count = 0
count2 = 0

for x in list_temps:
    if x < 0:
        count += 1

for x in list2_temps:
    if x < 0:
        count2 += 1

print(count)
print(count2)