def solution2(arr):
    new = list(arr)
    length = len(new)
    new_list = []
    for i in range(length):
        if i != 0 and i % 3 == 0:
            new[i] = ' '
        if new[i] == "h":
            new[i] = "H"
        if new[i] == "1":
            new[i] = "one"

    new_list.append(new[0])
    i = 1
    while i < length:
        if i % 3 != 0:
            new_list.append(new[i])
        i += 1

    listToStr = ''.join([str(elem) for elem in new_list])
    return listToStr


text = "1+1=2"

print(list(text))
print(solution2(text))
