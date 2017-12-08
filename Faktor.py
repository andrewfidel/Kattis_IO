
"""
Faktor

Input: the number of articles you plan to publish
       The impact Factor the owners require

Output: The minimal number of scientists you need to bribe (Minimum total count of citations)

https://open.kattis.com/problems/faktor
"""

# num_articles_to_publish = int(input())
# impact_factor_required = input(input())

# num_articles_to_publish = 38
# impact_factor_required = 24
# citations = 1
# output = 0
#
# while output < impact_factor_required:
#     output = citations/num_articles_to_publish
#     citations += 1
#
# print(output)

def main():
    num_articles_to_publsh = 38
    impact_factor_required = 24

    impact_factor_required = impact_factor_required - 1

    output = (impact_factor_required * num_articles_to_publsh) + 1
    print output

main()
