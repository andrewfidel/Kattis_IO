num = 13
binary = '{0:b}'.format(num)
new_word = ""

for i in range(1, len(binary) + 1):
    new_word += binary[len(binary) - i]

new_word = int(new_word, 2)

print(new_word)



