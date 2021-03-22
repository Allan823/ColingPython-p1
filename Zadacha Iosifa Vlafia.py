def josephus(ls, skip):
    skip -= 1 
    idx = skip
    while len(ls) > 1:
        print(ls.pop(idx)) 
        idx = (idx + skip) % len(ls)
    print('survivor: ', ls[0])


output

josephus([1,2,3,4,5,6,7], 3)
3
6
2
7
5
1
survivor:  4
