""""

https://open.kattis.com/problems/judgingmoose
https://repl.it/repls/FamousOffbeatDunnart
"""

input = input().split()

left_tine = int(input[0])
right_tine = int(input[1])
total = left_tine + right_tine

if left_tine == 0 and right_tine == 0:
    print("Not a moose")

elif total % 2 == 0:
    print('{}{}'.format("Even ", total))

else:
    print('{}{}'.format("Odd ", total))