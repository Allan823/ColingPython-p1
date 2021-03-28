
def solution(a, b):
    new_list = []
    a=set(a)
    d = list(a)+b
    while d:
        new_list.append(d.pop(d.index(min(d)))) 
    return new_list


#a = [1, 1, 2, 5]
#b = [1, 3, 4, 5, 8]
#solution(a, b)
