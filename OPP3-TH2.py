class SieuNhan:
    ten=str
    vukhi=str
    mausac=str
    def __init__(self,ten="",vukhi="",mausac=""):
        self.ten=ten
        self.vukhi=vukhi
        self.mausac=mausac
    def __str__(self):
        return "Ten: %s, Vu khi: %s, Mau sac: %s"%(self.ten,self.vukhi,self.mausac)
    sieuNhanA=SieuNhan("Sieu nhan do","Kiem","Do")
    sieuNhanB=SieuNhan("Sieu nhan xanh","Sung","Xanh")
    print(sieuNhanA)
    print(sieuNhanB)
