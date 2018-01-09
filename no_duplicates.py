""""

https://open.kattis.com/problems/nodup
https://repl.it/repls/ShoddySuperBagworm

different inputs:
THE RAIN IN SPAIN

IN THE RAIN AND THE SNOW

"""

string_input = input().split()
flag = True

for i in string_input:
    count = string_input.count(i)
    if count > 1:
        print("no")
        flag = False
        break
    else:
        continue

if flag is True:
    print("yes")


