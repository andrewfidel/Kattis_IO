""""

https://open.kattis.com/problems/pet
https://repl.it/repls/SnappyEnormousMule
"""

import operator

contestant1 = input().split()
master = []

list1 = []
for i in contestant1:
  list1.append(int(i))
cont1_sum = sum(list1)
master.append(cont1_sum)

contestant2 = input().split()
list2 = []
for i in contestant2:
  list2.append(int(i))
cont2_sum = sum(list2)
master.append(cont2_sum)

contestant3 = input().split()
list3 = []
for i in contestant3:
  list3.append(int(i))
cont3_sum = sum(list3)
master.append(cont3_sum)

contestant4 = input().split()
list4 = []
for i in contestant4:
  list4.append(int(i))
cont4_sum = sum(list4)
master.append(cont4_sum)

index, value = max(enumerate(master, start = 1), key=operator.itemgetter(1))
print('%s %s' % (index, value))