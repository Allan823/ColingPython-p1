class OneIndexedList():
        def __init__(self, elements=0):
            self.items = [0] * elements

        def __getitem__(self, index):
            if len(self.items) == 0:
                print("List is Empty")
            else:
                print(self.items[index-1])

        def __setitem__(self):
            return str(self.items)

a=OneIndexedList()
a.items.append(1)
a[1]

