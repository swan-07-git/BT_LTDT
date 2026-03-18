class NhanVien:
    LUONG_MAX = 20000  
    def __init__(self, tenNhanVien, luongCoBan, heSoLuong):
        self.tenNhanVien = tenNhanVien
        self.luongCoBan = luongCoBan
        self.heSoLuong = heSoLuong
    def getTenNhanVien(self):
        return self.tenNhanVien
    def setTenNhanVien(self, ten):
        self.tenNhanVien = ten
    def getLuongCoBan(self):
        return self.luongCoBan
    def setLuongCoBan(self, luong):
        self.luongCoBan = luong
    def getHeSoLuong(self):
        return self.heSoLuong
    def setHeSoLuong(self, hsl):
        self.heSoLuong = hsl
    def tinhLuong(self):
        return self.luongCoBan * self.heSoLuong
    def inTTin(self):
        print(f"Tên: {self.tenNhanVien}")
        print(f"Lương cơ bản: {self.luongCoBan}")
        print(f"Hệ số lương: {self.heSoLuong}")
        print(f"Lương thực nhận: {self.tinhLuong()}")
    def tangLuong(self, delta):
        luong_moi = self.tinhLuong() + delta
        if luong_moi > NhanVien.LUONG_MAX:
            print("Không thể tăng lương: vượt quá LUONG_MAX!")
            return False
        else:
            self.heSoLuong = luong_moi / self.luongCoBan
            print("Tăng lương thành công.")
            return True
