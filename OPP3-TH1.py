class Point:
    __x=int
    __y=int
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def setXY(self,x=3,y=5):
        if isinstance(X,int) and isinstance(y,int):
                      self.__x=y
                      self.__y=y
p1=Point()
print(p1.getX())
p1.setXY(3,5)
print(p1.getX())
