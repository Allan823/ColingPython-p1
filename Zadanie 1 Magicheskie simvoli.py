class OneIndexedList:

  def _init_(self, *args):
      self.values = list(args)

  def _setitem_(self):
        return str(self.values)


  def _getitem_(self, item):
        if 0<=item<len(self.values):
            return self.values(item)

        else:
            raise IndexError("Индекс за границей нашей коллекции")


#a = [1,2,3,5,6]

# a = [1]

>>> 2
