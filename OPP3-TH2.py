class DogCat:
    name=str
    age=int
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
    def __str__(self):
        return "Ten: %s, Tuoi: %d"%(self.name,self.age)
dogcat1=DogCat("nguyenducanh",19)
dogcat2=DogCat("tranduykhanh",19)
print(dogcat1)      
print(dogcat2)
