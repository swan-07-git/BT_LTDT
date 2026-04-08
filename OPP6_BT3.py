import math
class MauSoBangKhong(Exception):
    def __init__(self):
        super().__init__("Lỗi: Mẫu số không thể bằng 0!")
class PhanSo:
    def __init__(self, tu, mau):
        self.__tu_so = tu
        self.mau_so = mau 
    @property
    def tu_so(self):
        return self.__tu_so
    @tu_so.setter
    def tu_so(self, value):
        self.__tu_so = value
    @property
    def mau_so(self):
        return self.__mau_so
    @mau_so.setter
    def mau_so(self, value):
        if value == 0:
            raise MauSoBangKhong()
        self.__mau_so = value
    def toi_gian(self):
        ucln = math.gcd(self.__tu_so, self.__mau_so)
        dau = 1 if self.__mau_so > 0 else -1
        return PhanSo((self.__tu_so // ucln) * dau, abs(self.__mau_so // ucln))
    def is_toi_gian(self):
        return math.gcd(self.__tu_so, self.__mau_so) == 1
    def __add__(self, other):
        moi_tu = self.__tu_so * other.mau_so + other.tu_so * self.__mau_so
        moi_mau = self.__mau_so * other.mau_so
        return PhanSo(moi_tu, moi_mau).toi_gian()
    def __sub__(self, other):
        moi_tu = self.__tu_so * other.mau_so - other.tu_so * self.__mau_so
        moi_mau = self.__mau_so * other.mau_so
        return PhanSo(moi_tu, moi_mau).toi_gian()
    def __mul__(self, other):
        return PhanSo(self.__tu_so * other.tu_so, self.__mau_so * other.mau_so).toi_gian()
    def __truediv__(self, other):
        return PhanSo(self.__tu_so * other.mau_so, self.__mau_so * other.tu_so).toi_gian()
    def __eq__(self, other):
        s1 = self.toi_gian()
        s2 = other.toi_gian()
        return s1.tu_so == s2.tu_so and s1.mau_so == s2.mau_so
    def __lt__(self, other):
        s1 = self.toi_gian()
        s2 = other.toi_gian()
        return s1.tu_so * s2.mau_so < s2.tu_so * s1.mau_so
    def __gt__(self, other):
        return not self.__lt__(other) and not self.__eq__(other)
    def __str__(self):
        ps = self.toi_gian()
        if ps.mau_so == 1:
            return f"{ps.tu_so}"
        return f"{ps.tu_so}/{ps.mau_so}"
    def __repr__(self):
        return f"PhanSo({self.__tu_so}, {self.__mau_so})"
    def __hash__(self):
        ps = self.toi_gian()
        return hash((ps.tu_so, ps.mau_so))
try:
    ds_phanso = [PhanSo(1, 2), PhanSo(4, 2), PhanSo(3, 4), PhanSo(2, 4)]
    print("Dãy phân số ở dạng tối giản:")
    for ps in ds_phanso:
        print(f"{ps.toi_gian()}") 
    print("\nDãy phân số sau khi sắp xếp tăng dần:")
    for ps in sorted(ds_phanso):
        print(ps)
except MauSoBangKhong as e:
    print(e)
