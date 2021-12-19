
class Shape():
    def area(self):
        area=0


class Square(Shape):
    def __init__(self,length):
        self.len=length
        
    
    def area(self):
        return self.len*self.len
    
if __name__=="__main__":
    obj1=Square(30)
    print(obj1.area())
