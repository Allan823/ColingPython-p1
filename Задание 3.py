def integers():
    i = 1
    while True:
        yield i
        i += 1


def square(num):
    nums = []
    for x in integers():
        if x <=num:
            nums.append(pow(x, 2))
        if x > num:
            break
    return nums


def take(num):
    return square(num)


print(take(5))
