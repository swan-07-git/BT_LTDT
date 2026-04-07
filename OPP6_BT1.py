from abc import ABC, abstractmethod
from datetime import dat
class GiaKhongHopLe(Exception):
    def __init__(self, gia):
        self.gia = gia
        super().__init__(f"Lỗi: Giá {gia:,.0f}đ không hợp lệ (phải >= 0)")
class HangHoa(ABC):
    def __init__(self, ma, ten, nsx, gia):
        self.__ma = ma
        self.__ten = ten
        self.__nsx = nsx
        self.gia = gia  
    @property
    def ma_hang(self): return self.__ma

    @property
    def gia(self): return self.__gia

    @gia.setter
    def gia(self, value):
        if value < 0:
            raise GiaKhongHopLe(value) 
        self.__gia = value

    @abstractmethod
    def loai_hang(self): 
        pass
    def inTTin(self):
        return f"[{self.loai_hang()}] {self.__ma} | {self.__ten} | NSX: {self.__nsx} | Giá: {self.__gia:,.0f}đ"
    def __str__(self): return self.inTTin() 
    def __eq__(self, other): return self.__ma == other.__ma 
    def __lt__(self, other): return self.__gia < other.__gia 
    def __hash__(self): return hash(self.__ma)
class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bh, dap, cs):
        super().__init__(ma, ten, nsx, gia)
        self.__bh, self.__dap, self.__cs = bh, dap, cs
    def loai_hang(self): return "Điện máy"
    def inTTin(self):
        return f"{super().inTTin()} | BH: {self.__bh}th | {self.__dap}V - {self.__cs}W"
class HangSanhSu(HangHoa):
    def __init__(self, ma, ten, nsx, gia, nguyen_lieu):
        super().__init__(ma, ten, nsx, gia)
        self.__nguyen_lieu = nguyen_lieu
    def loai_hang(self): return "Sành sứ"
    def inTTin(self):
        return f"{super().inTTin()} | Nguyên liệu: {self.__nguyen_lieu}"
class HangThucPham(HangHoa):
    def __init__(self, ma, ten, nsx, gia, ngay_sx, ngay_hh):
        super().__init__(ma, ten, nsx, gia)
        self.__ngay_sx = ngay_sx
        self.__ngay_hh = ngay_hh

    def loai_hang(self): return "Thực phẩm"
    def inTTin(self):
        return f"{super().inTTin()} | NSX: {self.__ngay_sx} | HSD: {self.__ngay_hh}"
kho_hang = [
    HangDienMay("DM01", "Tủ lạnh LG", "LG", 15000000, 24, 220, 150),
    HangSanhSu("SS01", "Bình hoa Chu Đậu", "Chu Đậu", 2000000, "Gốm"),
    HangThucPham("TP01", "Sữa tươi", "Vinamilk", 30000, date(2023,1,1), date(2023,6,1)),
    HangDienMay("DM02", "Máy giặt Sony", "Sony", 12000000, 12, 220, 2000)
]
print("--- DANH SÁCH HÀNG HÓA TRONG KHO (ĐÃ SẮP XẾP THEO GIÁ TĂNG DẦN) ---")
for sp in sorted(kho_hang):
    print(sp) 
try:
    sp_loi = HangDienMay("ERR", "Lỗi giá", "X", -100, 0, 0, 0)
except GiaKhongHopLe as e:
    print(f"\n[THÔNG BÁO LỖI]: {e}")
