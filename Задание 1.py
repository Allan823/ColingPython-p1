class OneIndexedList:
    def __init__(self, items = []):
        self.items = items

    def __setitem__(self, index, item):
        self.items[index - 1] = item

    def __getitem__(self, index):
        return self.items[index - 1]

    def __str__(self):
        return f'{self.items}'


#a = OneIndexedList([1,2,3])

#a[1]

#a = OneIndexedList()
#a.items.append(0)

#a[1]
    
