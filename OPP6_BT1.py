from abc import ABC, abstractmethod
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
        return f"[{self.loai_hang()}] {self.__ma} | {self.__ten} | {self.__gia:,.0f}đ"
    def __str__(self): 
        return self.inTTin() 
    def __eq__(self, other): 
        return self.__ma == other.ma_hang     
    def __lt__(self, other): 
        return self.__gia < other.gia    
    def __hash__(self): 
        return hash(self.__ma)
class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, bh, dap, cs):
        super().__init__(ma, ten, nsx, gia)
        self.__bh, self.__dap, self.__cs = bh, dap, cs
    def loai_hang(self):
        return "Điện máy"
    def inTTin(self):
        return f"{super().inTTin()} | BH: {self.__bh}th | {self.__dap}V - {self.__cs}W"

try:
    sp = HangDienMay("A", "Điều hòa", "AKITO", 6868686868686, 99, 999, 9999)
    print(sp)
except GiaKhongHopLe as e:
    print(e)
