def solution(arr):
    arr.append(0)
    arr.insert(0, arr[0] - 1)
    temp = 0
    num = 0
    final_num = 0
    for i in range(len(arr)):
        if temp == arr[i]:
            num += 1
        elif temp != arr[i]:
            if final_num < num:
                final_num = num
                num = 0
            temp = arr[i]
    return final_num + 1


array = [1,1,1,1,1,2,3,3,2,100,15,15,15]
print(solution(array))



