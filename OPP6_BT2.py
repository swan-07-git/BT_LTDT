from abc import ABC, abstractmethod
class CanBoError(Exception):
    pass
class TuoiKhongHopLe(CanBoError):
    def __init__(self, tuoi):
        super().__init__(f"Lỗi: Tuổi {tuoi} không hợp lệ (yêu cầu từ 18 - 65)")
class BacKhongHopLe(CanBoError):
    def __init__(self, bac):
        super().__init__(f"Lỗi: Bậc {bac} không hợp lệ (yêu cầu từ 1 - 10)")
class CanBo(ABC):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi):
        self.__ho_ten = ho_ten
        self.tuoi = tuoi
        self.__gioi_tinh = gioi_tinh
        self.__dia_chi = dia_chi

    @property
    def ho_ten(self): return self.__ho_ten
    @property
    def tuoi(self): return self.__tuoi

    @tuoi.setter
    def tuoi(self, value):
        if not (18 <= value <= 65):
            raise TuoiKhongHopLe(value)
        self.__tuoi = value
    @abstractmethod
    def mo_ta(self):
        pass
    def __str__(self):
        return f"{self.__ho_ten} | Tuổi: {self.__tuoi} | GT: {self.__gioi_tinh} | {self.mo_ta()}"
    def __eq__(self, o):
        return self.__ho_ten == o.__ho_ten and self.__tuoi == o.__tuoi
    def __lt__(self, o):
        return self.__ho_ten < o.__ho_ten

class CongNhan(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, bac):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.bac = bac
    @property
    def bac(self): return self.__bac
    @bac.setter
    def bac(self, value):
        if not (1 <= value <= 10):
            raise BacKhongHopLe(value)
        self.__bac = value
    def mo_ta(self): return f"Công nhân bậc {self.__bac}"

class KySu(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, nganh):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__nganh = nganh
    def mo_ta(self): return f"Kỹ sư ngành {self.__nganh}"

class NhanVien(CanBo):
    def __init__(self, ho_ten, tuoi, gioi_tinh, dia_chi, cong_viec):
        super().__init__(ho_ten, tuoi, gioi_tinh, dia_chi)
        self.__cong_viec = cong_viec
    def mo_ta(self): return f"Nhân viên: {self.__cong_viec}"

ds_can_bo = [
    CongNhan("Nguyễn Thị A", 19, "Nữ", "Hà Tĩnh  ", 7),
    KySu("Trần Thị B", 25, "Nữ", "TP.HCM", "CNTT"),
    NhanVien("Lê Văn C", 40, "Nam", "Đà Nẵng", "Kế toán")
]

print(" DANH SÁCH CÁN BỘ (ĐÃ SẮP XẾP) ")
for cb in sorted(ds_can_bo):
    print(cb)
try:
    with open("canbo.txt", "w", encoding="utf-8") as f:
        for cb in ds_can_bo:
            f.write(str(cb) + "\n")
    print("\nĐã lưu danh sách vào file canbo.txt")
except Exception as e:
    print(f"Lỗi ghi file: {e}")
