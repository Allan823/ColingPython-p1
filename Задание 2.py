class ReverseIter:
    def __init__(self, list):
        self.list = reversed(list)
        self.list = iter(self.list)


num = ReverseIter([1, 2, 3, 4])
print(next(num.list))
print(next(num.list))
print(next(num.list))
print(next(num.list))

