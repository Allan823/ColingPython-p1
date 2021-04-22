def solution(a):
    b = set(sorted(a))
    a = 1
    for x in b:
        if x == a:
            a-=1
    return a



#solution([1,2,3])
