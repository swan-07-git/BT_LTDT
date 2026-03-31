class CanBo:
    def __init__(self,ten,tuoi,gioitinh,diachi):
        self.ten=ten
        self.tuoi=tuoi
        self.gioitinh=gioitinh
        self.diachi=diachi
    def loai_canbo(self):
        return"Cán Bộ"
    def hien_thi(self):
        print(f"{self.loai_canbo()}: {self.ten}")
        print(f"Tuổi: {self.tuoi}")
        print(f"Giới tính: {self.gioitinh}")   
        print(f"Địa chỉ: {self.diachi}")
    class CongNHan:
        def __init__(self,ten,tuoi,gioitinh,diachi,bac):
            super().__init__(ten,tuoi,gioitinh,diachi)
            if not(1<=bac<=10):
                raise ValueError(" 1 - 10")
            self.__bac=bac
        def loai_canbo(self):
            return"Công Nhân"
        def hien_thi(self):
            super().hien_thi()
            print(f"Bậc: {self.bac}")
    cb1=CanBo("Minh",19,"Nữ","Thanh Hóa" )
    cb1.hien_thi()


