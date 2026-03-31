class HangHoa:
    def __init__(self, ma, ten, nsx, gia):
        self.ma_hang = ma
        self.ten_hang = ten
        self.nha_sx = nsx
        self.gia = gia

    def __str__(self):
        return f"Mã: {self.ma_hang}, Tên: {self.ten_hang}, Giá: {self.gia}"

class HangDienMay(HangHoa):
    def __init__(self, ma, ten, nsx, gia, tg_baohanh, dien_ap, cong_suat):
        super().__init__(ma, ten, nsx, gia) # Gọi constructor lớp cha [4]
        self.tg_baohanh = tg_baohanh
        self.dien_ap = dien_ap
        self.cong_suat = cong_suat

class HangThucPham(HangHoa):
    def __init__(self, ma, ten, nsx, gia, ngay_sx, ngay_hethan):
        super().__init__(ma, ten, nsx, gia)
        self.ngay_sx = ngay_sx
        self.ngay_hethan = ngay_hethan