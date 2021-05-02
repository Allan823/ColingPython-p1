def solution(n,k):
    k -= 1 
    idx = k
    while len(n) > 1:
        print(n.pop(idx))
        idx = (idx + k) % len(n)
    return f"solution:{n[0]}"

    #print('survivor:', n[0])




#solution([1,2,3,4,5,6,7], 3)

