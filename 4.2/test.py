from itertools import combinations

def solution(num_buns, num_required):
    keyrings = [[] for num in range(num_buns)]

    print(keyrings)


    copies_per_key = num_buns - num_required + 1

    print(range(num_buns), copies_per_key)

    x = combinations(range(num_buns), copies_per_key)
    print(x)

    for i in x:
        print(i)

    print("---")

    # print()

    x = combinations(range(num_buns), copies_per_key)
    for i in enumerate(x):
        print(i)

    x = combinations(range(num_buns), copies_per_key)
    print(enumerate(x))
    print("---")

    x = combinations(range(num_buns), copies_per_key)
    for key, bunnies in enumerate(x):

        print(key, bunnies)
        for bunny in bunnies:
            keyrings[bunny].append(key)

    return keyrings

solution(5, 3)