def solution(x, y):
  x1 = set(x)
  y1 = set(y)

  for item in x:
    if (item in y1) == False:
      return item

  for item in y:
    if (item in x1) == False:
      return item
  return 0

print(solution([14, 27, 1, 4, 2, 50, 3, 1], [2, 4, -4, 3, 1, 1, 14, 27, 50]))

print(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]))