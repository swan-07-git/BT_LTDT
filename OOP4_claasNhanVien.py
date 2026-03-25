class NhanVien:
   def __init__(sef,ten,luongCB,heSo,luongMax):
       self.__tenNhanVien=ten
       self.__luongCoBan=luongCB
       self.__heSoLuong=heSo
       self.__LUONG__MAX=luongMax
   def geTenNhanVien(self):
      return self.__tenNhanVien
   def getluongCoBan(self):
      return self.__luongCB
   def setLuongCoBan(self,luong):
      self.__luongCoBan=luong
   def getHeSoLuong(self):
       return self.__heSoLuong
   def setHeSoLuong(self,heSo):
      self.__heSoLuong=heSo
   def tinhLuong(self):
      return self.__luongCoBan*self.__heSoLuong
   def tangLuong(self,luongTang):
      heSoMoi= self.__heSoLuong+luongTang
      if (self.__luongCoBan*heSoMoi)>self.LUONG_MAX:
         print("Lương sau khi tăng vượt quá lương tối đa cho phép")
         return False
      else:
          self.heSoLuong=heSoMoi
          return True
   def inTTin(self):
       print(f"Nhân viên: {self.__tenNhanVien}")
       print(f"Lương cơ bản: {self.__luongCoBan}")
       print(f"Hệ số lương: {self.__heSoLuong}")
       print(f"Lương hiện tại: {self.tinhLuong()}")
            
