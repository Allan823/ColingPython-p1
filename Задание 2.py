from collections import Counter

string = "gjdkfnvjkenrvbfceabdcaagcbbcabacd"

obj = Counter(string)
items = obj.items()


def min(arr):
    min1 = True
    for x in range(len(arr)):
        if arr[x] == False:
            min1 = False
    return min1


def search(x, str):
    if x in str:
        return False
    else:
        return True


str1 = ''


def stro(items, str1):
    arr = []
    for x in items:
        for y in items:
            if ord(x[0]) <= ord(y[0]) and search(x[0], str1):
                arr.append(True)
            else:
                arr.append(False)
        if min(arr):
            for z in range(x[1]):
                str1 += x[0]
            obj.pop(x[0])
            break
        arr.clear()
    if len(items) == 0:
        return str1
    else:
        return stro(obj.items(), str1)

print(string)
print(stro(items, str1))
