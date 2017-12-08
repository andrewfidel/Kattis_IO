"""
Oddities

For each x, print either 'x is odd' or 'x is even' depending on whether x is odd or even

"""

multiplier = int(input())
first_input = int(input())
second_input = int(input())
third_input = int(input())
# multiplier = 3
# first_input = 10
# second_input = 9
# third_input = -5

output1 = first_input * multiplier
output2 = second_input * multiplier
output3 = third_input * multiplier

if(output1 % 2 == 0):
    print("{}{}".format(first_input, " is even"))
else:
    print("{}{}".format(first_input, " is odd"))

if(output2 % 2 == 0):
    print("{}{}".format(second_input, " is even"))
else:
    print("{}{}".format(second_input, " is odd"))
    
if(output3 % 2 == 0):
    print("{}{}".format(third_input, " is even"))
else:
    print("{}{}".format(third_input, " is odd"))
