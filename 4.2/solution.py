from itertools import combinations

def solution(num_buns, num_required):

    x = [ [] for n in range(num_buns)]


    answer = []
    for i in range(num_buns):
        answer.append([])


    max_copies = num_buns - num_required + 1
    distributed_key = combinations(range(num_buns), max_copies)

    for key, holder in enumerate(distributed_key):
        for i in holder:
            answer[i].append(key)

    print(answer)
    return answer


solution(2, 1)
solution(4, 4)
solution(5, 3)
