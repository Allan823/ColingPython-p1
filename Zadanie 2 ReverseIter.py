class ReverseIter(object):
    def __init__(self, ls):
        self.a = list(reversed(ls))
 
    def __str__(self):
        return str(self.a)
 
 
it = ReverseIter([10, 54, 12,0])
print(it)

