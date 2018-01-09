"""

https://open.kattis.com/problems/sibice
https://repl.it/repls/ShabbyOtherAldabratortoise

inputs:
5 3 4
3
4
5
6
7
"""


first_input = input().split()
num_matches = int(first_input[0])
height = int(first_input[1]) * int(first_input[1])
width = int(first_input[2]) * int(first_input[2])
total_size = height+width

list = []
input1 = int(input())
input1 = input1 * input1
input2 = int(input())
input2 = input2 * input2
input3 = int(input())
input3 = input3 * input3
input4 = int(input())
input4 = input4 * input4
input5 = int(input())
input5 = input5 * input5


list.append(input1)
list.append(input2)
list.append(input3)
list.append(input4)
list.append(input5)

# for x in list:
#   if x < total_size:
#     print("DAE")
#   else:
#     print("NAE")

for x in list:
  if x > total_size:
    print("NAE")
  else:
    print("DAE")

