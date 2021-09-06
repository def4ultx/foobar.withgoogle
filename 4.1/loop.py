l = [(21,21,False),
    (21,19,True),
    (21,13,True),
    (21,7,False),
    (21,3,False),
    (21,1,True),
    (19,13,False),
    (19,7,True),
    (19,3,True),
    (19,1,True),
    (13,7,True),
    (13,3,False),
    (13,1,True),
    (7,3,True),
    (7,1,False),
    (3,1,False),
    (1,1,False)]


# def loop(x, y):
#     z = x + y
#     while y:
#         x, y = y, y % x
#     z //= x
#     return (z & (z - 1)) != 0


def dead_lock(x,y):
    if x == y:
        return 0


    if (x+y) % 2 == 1:
        return 1

    l = gcd(x,y)
    x,y = x/l,y/l
    x,y = max(x,y), min(x,y)    
    return dead_lock(x-y,2*y)

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x
    
from fractions import gcd
def loop(x, y):
    if x == y:
        return False
    if x < y:
        x, y = y, x

    if (x+y) % 2 == 1:
        return 1

    l = gcd(x,y)
    x,y = x/l,y/l
    x, y = x - y, y * 2

    return loop(x, y)

# def loop(a, b):
#     compute = {}

#     def cal(x, y):
#         if x == y:
#             return False
#         if x < y:
#             x, y = y, x
#         # print("compute", compute)
#         # print(x, y)
#         # compute.add((x, y))

#         if (x+y) % 2 == 1:
#             return 1

#         l = gcd(x,y)
#         x,y = x/l,y/l
#         x, y = x - y, y * 2

#         if (x, y) in compute:
#             # print("return", compute.get((x,y)))
#             return True
#         # compute[(x,y)] = True
#         # print(x, y)
#         # print("end")
#         # if x == y:
#             # compute[(x,y)] = False
#             # return False
#         # else:
#             # print(x,y,"added")
#         compute[(x,y)] = True
#             # return cal(x, y)
#         return cal(x, y)
#     return cal(a, b)

def is_forever(x, y):
    if (x == y):
        return False
    if y > x:
        x, y = y, x  # Swap them for an integer division.
    if (x % y != 0):
        return True
    z, r = divmod(x, y)
    print(z, r)
    if r:
        return True  # Indivisible
    # (z - 1) & z is False for a power of two, but c should be False
    # for a power of two - 1, so add one on both sides.
    return bool(z & (z + 1))

# print(is_forever(13,7), "result")

for (x,y,z) in l:
    if z != loop(x,y):
        print(x, y, "expected", z)

for i in range(10000, 20000):
    if i % 50 == 0:
        print("loop", i)
    for j in range(10000, 20000):
        # x = dead_lock(i,j)
        y = loop(i,j)

        # if x != y:
        #     print(i,j,x,y)
    

# import unittest

# class TestStringMethods(unittest.TestCase):

#     def test_loop(self):
#         for (x,y,expected) in l:
#             actual = loop(x,y)
#             self.assertEqual(result, z)

# if __name__ == '__main__':
#     unittest.main()
