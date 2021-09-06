def answer(banana_list):
    banana_list.sort(reverse=True)
    n = len(banana_list)

    print(banana_list)

    def isLoop(x, y):
        z = x + y
        while y:
            x, y = y, y % x
        z //= x
        return (z & (z - 1)) != 0

    graph = {}
    for i in range(n - 1):
        for j in range(i + 1, n):
            # print(i, j, " -- ", banana_list[i], banana_list[j])
            if isLoop(banana_list[i], banana_list[j]):
                print(i, j, " -- ", banana_list[i], banana_list[j])
                graph.setdefault(i, [])
                graph.setdefault(j, [])
                graph[i].append(j)
                graph[j].append(i)

    # print(graph)

    return maximum_matching(graph, n)


def maximum_matching(graph, size):
    exposed = list(range(size))
    nonmatch_e = set([(x, y) for x in graph for y in graph[x]])
    match_e = set()

    # print('\n')
    # print("max matching")

    # print(exposed)

    # print(nonmatch_e)

    # print(match_e)

    # print("-----")
    # print('\n')

    hasPath = True
    while hasPath:
        hasPath = False
        for start in exposed:

            visited = set()
            flag = False
            path = []
            u = start


            while True:
                visited.add(u)

                # print("started")
                # print("u", u)
                # print("path", path)
                # print("flag", flag)
                # print("u graph", graph.get(u, []))

                # x, y = -1, -1
                for v in graph.get(u, []):
                    if v in visited:
                        continue
                    if (not flag and (u, v) in nonmatch_e) or (flag and (u, v) in match_e):
                        # x, y = u, v
                        path.append(u)
                        path.append(v)
                        break

                # # print("path", path)
                # print("new path", path)
                # # print("x,y:", x,y)
                # print("exposed", exposed)
                # if x == -1 and y == -1:
                #     break
                if not path:
                    break

                # print("continue", path[-1], start)
                # print("continue", path[-1] in exposed, path[-1] != start)

                # print('path[-1]', path[-1], start)
                # if y != start: # y != start
                #     hasPath = True
                #     if (x, y) in match_e:
                #         match_e.remove((x, y))
                #         match_e.remove((y, x))
                #         nonmatch_e.add((x, y))
                #         nonmatch_e.add((y, x))
                #     else:
                #         nonmatch_e.remove((x, y))
                #         nonmatch_e.remove((y, x))
                #         match_e.add((x, y))
                #         match_e.add((y, x))
                #     # exposed.remove(x)
                #     # exposed.remove(y)
                #     break

                if path[-1] in exposed and path[-1] != start: # path[-1] != start
                    hasPath = True

                    # print("path len", len(path))
                    # print("match", match_e)
                    # print("non_match", nonmatch_e)
                    # print("----", path[0], path[1])

                    for i in range(len(path) - 1):
                        if (path[i], path[i + 1]) in match_e:
                            match_e.remove((path[i], path[i + 1]))
                            match_e.remove((path[i + 1], path[i]))
                            nonmatch_e.add((path[i], path[i + 1]))
                            nonmatch_e.add((path[i + 1], path[i]))
                        else:
                            nonmatch_e.remove((path[i], path[i + 1]))
                            nonmatch_e.remove((path[i + 1], path[i]))
                            match_e.add((path[i], path[i + 1]))
                            match_e.add((path[i + 1], path[i]))

                    # exposed.remove(path[0])
                    # exposed.remove(path[-1])
                    # print("break")
                    break

                flag = not flag
                u = path.pop()
            #     print("pop u", u)
            # print("end loop")
            # print("expose", exposed)
            # print('\n')

    # print("match", match_e)
    # print("non_match", nonmatch_e)

    for (x, y) in match_e:
        if x in exposed:
            exposed.remove(x)
        
        if y in exposed:
            exposed.remove(y)

    print(len(exposed))
    return len(exposed)

# print(answer([1073741723,1073741724,1073741725,1073741726,1073741727,1073741728,1073741729,1073741730,1073741731,1073741732,1073741733,1073741734,1073741735,1073741736,1073741737,1073741738,1073741739,1073741740,1073741741,1073741742,1073741743,1073741744,1073741745,1073741746,1073741747,1073741748,1073741749,1073741750,1073741751,1073741752,1073741753,1073741754,1073741755,1073741756,1073741757,1073741758,1073741759,1073741760,1073741761,1073741762,1073741763,1073741764,1073741765,1073741766,1073741767,1073741768,1073741769,1073741770,1073741771,1073741772,1073741773,1073741774,1073741775,1073741776,1073741777,1073741778,1073741779,1073741780,1073741781,1073741782,1073741783,1073741784,1073741785,1073741786,1073741787,1073741788,1073741789,1073741790,1073741791,1073741792,1073741793,1073741794,1073741795,1073741796,1073741797,1073741798,1073741799,1073741800,1073741801,1073741802,1073741803,1073741804,1073741805,1073741806,1073741807,1073741808,1073741809,1073741810,1073741811,1073741812,1073741813,1073741814,1073741815,1073741816,1073741817,1073741818,1073741819,1073741820,1073741821,1073741822]))
print(answer([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99]))

print("xxxxxxxxxxxxxxxx")
print(answer([1, 1]))
print("xxxxxxxxxxxxxxxx")
print(answer([1, 3, 7, 13, 19, 21]))
print("xxxxxxxxxxxxxxxx")
print(answer([1]))
# print(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 19]))
# print(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 12]))
# print(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 1]))
# print(answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 19, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))