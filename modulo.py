""""

https://open.kattis.com/problems/modulo
https://repl.it/repls/AccurateSneakyGosling

input:
1
2
3
4
5
6
7
8
9
10


"""
master = []
distinct_result = []
input1 = input()
input2 = input()
input3 = input()
input4 = input()
input5 = input()
input6 = input()
input7 = input()
input8 = input()
input9 = input()
input10 = input()

master.append(input1)
master.append(input2)
master.append(input3)
master.append(input4)
master.append(input5)
master.append(input6)
master.append(input7)
master.append(input8)
master.append(input9)
master.append(input10)

num = 0
for x in master:
    modulo_result = int(x) % 42
    distinct_result.append(modulo_result)
    count = distinct_result.count(modulo_result)
    if count == 1:
        num += 1

print(num)
