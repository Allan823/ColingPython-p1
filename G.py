def solution(a, b):
    new_list = []
    for i in b:
        if i in a:
            b.remove(i)
    c=a+b
    for i in range(0, len(c) - 1):
        smallest = i
        for j in range(i + 1, len(c)):
            if c[j] < c[smallest]:
                smallest = j
        c[i], c[smallest] = c[smallest], c[i] 
    return c


#a = [1, 1, 2, 5]

#b = [1, 3, 4, 5, 8]
# solution(a, b)
#[1, 1, 2, 3, 4, 5, 8]
