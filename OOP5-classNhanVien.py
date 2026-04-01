class NhanVien:
  def __init__(self,maNV,ten,nam,gioi,dc,heso,max_luong):
      self.__maNV=ma
      self.__hoten=ten
      self.__namsinh=nam
      self.__goiTinh=gioi
      self.__diachi=dc
      if heso <=0:
         raise ValueError("He so luong phai lon hon 0")
      self.__hesoLuong=heso
      self.luongMax=max_luong
  def get_hesoLuong(self):
      return self.__heSoLuong
  def get_LuongMax(self):
      return self.__luongMax
  def tinhThuNhap(self):
      luong=self.hesoLuong*180000
      return min(luong,self.__luongMax)
  def inTTin(self):
      print("ma NV : {self.maNV}}|Ho ten:{self.__hoTen}")
      print("Thu nhap :{self.tinhThuNhap():,.0}VND")
class CongTaxcVien(NhanVien):
  def __init__(self,ma,ten,gioi,nam,dc,heso,max_luong,thoi_han,phu_cap):
      super().__init__(ma,ten,nam,gioi,dc,heso,max_luong)
      self.__thoiHanHD=thoi_han
      self.__phuCapLD=phu_cap
  def tinhThuNhap(self):
       return super().tinhThuNhap() +self.__phuCapLD
class NhanVienChinhThuc:
  def __init__(self,ma,ten,gioi,nam,dc,heso,max_luong,vi_tri):
      super().__init__(ma,ten,nam,gioi,dc,heso,max_luong)
      self.__ngayBadauQL =ngay_ql
      self.__phuCapQL = phu_cap
  def tinhThuNhap(self):
      return super().tinhThunhap() +self.__phuCapQL
nv1=NhanVien("Nga", 2007, "Nữ", "Hà tĩnh", 5.0, 20000000, "01/04/2026", 2000000)
nv1.inTTin()

    
