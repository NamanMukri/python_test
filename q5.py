
class Student():
    def __init__(self,name,phy,chem,bio):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.bio=bio

    def total_obtained(self):
        self.sum=self.phy + self.chem + self.bio 
        return self.sum
        
    def percentage(self):
        self.totalmarks=300
        self.per=(self.total_obtained()/self.totalmarks)*100
        return int(self.per)


if __name__=="__main__":
    obj1=Student("naman",95,85,95)
    print(obj1.total_obtained())
    print(obj1.percentage())