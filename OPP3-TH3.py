ds_sieu_nhan = []

while True:
    ten = input("Nhập tên siêu nhân (hoặc 'stop' để dừng): ")
    if ten.lower() == "stop":
        break
    vu_khi = input("Nhập vũ khí: ")
    mau_sac = input("Nhập màu sắc: ")
    ds_sieu_nhan.append(SieuNhan(ten, vu_khi, mau_sac))

print("\nDanh sách siêu nhân:")
for sn in ds_sieu_nhan:
    print(sn)

