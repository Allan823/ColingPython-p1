def solution(x1,y1,x2,y2):
    a = x1-x2
    b = y1-y2
    if(a or b) >1 or (a or b) < -1:
        return False
    else:
        return True

print(solution(4,4,5,5))