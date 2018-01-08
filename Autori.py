""""

https://open.kattis.com/problems/autori
"""

sample_input = "Knuth-Morris-Pratt"
string = sample_input[0]

for x in range(0, len(sample_input)):
    if sample_input[x] == "-":
        string += sample_input[x+1]

print(string)


