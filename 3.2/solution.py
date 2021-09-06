import random

def solution(x, y):
    x = int(x)
    y = int(y)

    # print(x, y)

    count = 0
    cont = True


    while cont:
        if (x % y == 0 or y % x == 0) and (x != 1 and y != 1):
            # print("impossible")
            return "impossible"

        print("loop", count, x, y)
        if (x > y):
            count += x/y
            x = x%y
        elif (y > x):
            count += y/x
            y = y%x
        # if (x > y):
        #     x = x-y
        #     count += 1
        # elif (y > x):
        #     y = y-x
        #     count += 1

        print("end", count, x, y)
        if (x == 1 and y == 1):
            cont = False
        elif (x == 0 or y == 0):
            cont = False
            count -= 1

    # print(str(count))
    return str(count)

def getBigNumber(decNumber):
    decNumber
    for i in range(random.randint(10, 90)):
        decNumber = str(random.randint(0, 9)) + decNumber
    return decNumber

# print(solution("2", "1")) # 1
print(solution("4", "7")) # 4
print(solution("3", "5")) # 3
print(solution("1", "4")) # 3
# print("--")
# print(solution("2", "4")) # impossible
# print(solution("2", "2")) # impossible
# print("--")

# print("M:4, F:7", solution("4", "7"))
# print("------------------------------")
# print("M:2, F:7", solution("2", "7"))
# print("------------------------------")
# print("M:2, F:1", solution("2", "1"))
# print("------------------------------")
# print("M:14, F:7", solution("14", "7"))
# print("------------------------------")
# print("M:4, F:17", solution("4", "17"))
# print("------------------------------")
# print("M:41, F:7", solution("41", "7"))
# print("------------------------------")
# print("M:21, F:7", solution("21", "7"))
# print("------------------------------")
# print("M:22, F:7", solution("22", "7"))
# print("------------------------------")
# print("M:14, F:17", solution("14", "17"))
# print("------------------------------")
# print("M:50, F:7", solution("50", "7"))
# print("------------------------------")
# print("M:2, F:6456", solution("2", "6456"))
# print("------------------------------")
# print("M:BigNumber, F:7", solution(getBigNumber("1"), "7"))
# print("------------------------------")
# print("M:BigNumber, F:BigNumber", solution(getBigNumber("1"), getBigNumber("0")))