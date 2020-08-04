def solution(l):
    memory = {}

    def recursive(xs):
        if len(xs) == 0:
            return 0

        key = join(xs)
        if key in memory:
            return memory[key]

        import itertools
        temp = list(itertools.permutations(xs))

        m = find(temp)
        if m != 0:
            memory[key] = m
            return m

        arr = []
        # print(xs)
        for i in range(len(xs)):
            l = [x for x in xs]
            del l[i]

            # print(l)
            t = recursive(l)
            arr.append(t)

        m = max(arr)
        memory[key] = m
        return m

    l.sort(reverse=True)
    return recursive(l)

def find(xs):
    for x in xs:
        n = join(x)
        if n%3 == 0:
            return n
    return 0

def join(xs):
    if len(xs) == 0:
        return 0

    s = [str(i) for i in xs]
    return int("".join(s))

print(solution([3, 1, 4, 1])) # 4311
print(solution([3, 1, 4, 1, 5, 9])) # 94311
print(solution([3, 6, 4, 5])) # 94311
