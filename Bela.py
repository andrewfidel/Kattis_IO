
"""

https://open.kattis.com/problems/bela

"""

dominant = "S"
is_dominant = False
x = 0
dominant_dictionary = {

    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 20,
    "T": 10,
    "9": 14,
    "8": 0,
    "7": 0
}

notdominant_dictionary = {

    "A": 11,
    "K": 4,
    "Q": 3,
    "J": 2,
    "T": 10,
    "9": 0,
    "8": 0,
    "7": 0
}

hand = ["TH", "9C", "KS", "QS", "JS", "TD", "AD", "JH"]
count = 0

for x in hand:
    if x[1] == dominant:
        is_dominant = True
        count += dominant_dictionary[x[0]]
        is_dominant = False
    else:
        count += notdominant_dictionary[x[0]]


print(count)
