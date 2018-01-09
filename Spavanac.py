"""

https://open.kattis.com/problems/spavanac
https://repl.it/repls/PlumpImperfectFruitbat

inputs
10 10
0 30
23 40
"""

time = input().split()
x = int(time[0])  # input hours time
y = int(time[1])  # input minutes time
sixty_minute = 60
minutes_early = 45

difference = y - minutes_early
# if difference < 0:
new_difference = abs(difference)
new_hours_time = x - 1
new_minutes_time = sixty_minute - new_difference
if new_hours_time > 24:
    new_hours_time1 = 23
    print('{}{}{}'.format(new_hours_time1, ' ', new_minutes_time))
else:
    print('{}{}{}'.format(new_hours_time, ' ', new_minutes_time))

# else:
#   new_difference = difference
#   new_hours_time = x - 1
#   new_minutes_time = sixty_minute - new_difference
#   if new_hours_time > 24:
#     new_hours_time1 = 23
#     print('{}{}{}'.format(new_hours_time1,' ', new_minutes_time))
#   else:
#     print('{}{}{}'.format(new_hours_time,' ', new_minutes_time))





