def solution(arr1,arr2):
    for x in arr2:
        if x not in arr1:
            arr1.append(x)
    arr1.sort()
    return arr1

ar =  [1,1,2,5]
ar2 = [1,3,4,5,8]
print(solution(ar,ar2))