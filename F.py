def solution(num):
    arr = []
    number = 1
    while number <= num:
        arr.append(number)
        number =number*2
    return arr

print(solution(64))