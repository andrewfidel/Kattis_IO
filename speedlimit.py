""""
inputs
3
20 2
30 6
10 7


https://open.kattis.com/problems/speedlimit
https://repl.it/repls/MajesticHoarseUrson
"""

number_sets = input()
input1 = input().split()
input2 = input().split()
input3 = input().split()

set1 = []
set2 = []

set1.append(int(input1[1]))
difference = int(input2[1])-int(input1[1])
set1.append(difference)
difference2 = int(input3[1])-int(input2[1])
set1.append(difference2)

set2.append(int(input1[0]))
set2.append(int(input2[0]))
set2.append(int(input3[0]))

product = [x*y for x, y in zip(set1, set2)]
sum = sum(product)
print(sum)
