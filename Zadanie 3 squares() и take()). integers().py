def integers():
        i=1
        int_list=[]
        while i<=100:
                int_list.append(i)
                i+=1
        return int_list

def squares():
        squares=integers()
        new_squares=[]
        for square in squares:
                new_squares.append(square**2)
        return new_squares       

def take(count,list):
        i=0
        new_list=[]
        while i<=count:
                new_list.append(list[i])
                i+=1
        return new_list
print(take(5,squares()))
