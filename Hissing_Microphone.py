"""
Hissing Microphone

Input:
The input contains a single string on a single line.
This string consists of only lowercase letters (no spaces) and has between 11 and 3030 characters.

Output:
Output a single line. If the input string contains two consecutive occurrences of the letter s,
then output hiss. Otherwise, output no hiss.

"""

inputs = ["amiss", "octopuses", "hiss"]

inputamiss = "amiss"
input2 = "octopuses"
flag = False

for x in range(0, len(input2)):
    try:
        if input2[x] == input2[x+1]:
            flag = True
            print("hiss")
    except IndexError:
        break

if flag == False:
    print("no hiss")

