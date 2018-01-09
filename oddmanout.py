"""

https://open.kattis.com/problems/oddmanout
https://repl.it/repls/ClosedShortUrva

inputs:
3
3
1 2147483647 2147483647
5
3 4 7 4 3
5
2 10 2 10 5
"""

num_cases = input()

number_of_guests1 = input()
invitation_list1 = input().split()

for i in invitation_list1:
  count = invitation_list1.count(i)
  if count < 1:
    continue
  elif count == 1:
    print('{}{}'.format("Case #1: ", i))

number_of_guests2 = input()
invitation_list2 = input().split()

for i in invitation_list2:
  count = invitation_list2.count(i)
  if count < 1:
    continue
  elif count == 1:
    print('{}{}'.format("Case #2: ", i))


number_of_guests3 = input()
invitation_list3 = input().split()

for i in invitation_list3:
  count = invitation_list3.count(i)
  if count < 1:
    continue
  elif count == 1:
    print('{}{}'.format("Case #3: ", i))
