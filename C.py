arr = [[1,2,3], [8,9,4], [7,6,5]]
def solution(arr):
  a = []
    while arr:
        a.extend(list(arr.pop(0)))
        arr = list(zip(*arr))
        arr.reverse()
    return a
  print(solution(arr))
  
