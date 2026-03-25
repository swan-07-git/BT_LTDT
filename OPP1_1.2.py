print(42 * 60 + 42)
print(10 / 1.61)

tong_giay = 42 * 60 + 42
tong_dam = 10 / 1.61
giay_tren_moi_dam = tong_giay / tong_dam
phut_nhip_do = int(giay_tren_moi_dam // 60)
giay_nhip_do = int(giay_tren_moi_dam % 60)
print(f"Nhịp độ trung bình: {phut_nhip_do} phút {giay_nhip_do} giây mỗi dặm")
tong_gio = tong_giay / 3600
van_toc_mph = tong_dam / tong_gio
print(f"Vận tốc trung bình: {van_toc_mph} dặm/giờ")
