import math
from datetime import datetime, timedelta
#1
r = 5
volume = (4/3) * math.pi * r**3
print("1. Thể tích hình cầu bán kính 5 =", volume)
#2
cover_price = 24.95
discount_price = cover_price * 0.6   # giảm 40%
copies = 60
books_cost = discount_price * copies
shipping = 3 + (copies - 1) * 0.75
total_cost = books_cost + shipping
print("2. Tổng chi phí 60 cuốn sách =", total_cost)

# 3. Thời gian về nhà sau khi chạy
start_time = datetime.strptime("6:52", "%H:%M")
easy_pace = timedelta(minutes=8, seconds=15)
tempo_pace = timedelta(minutes=7, seconds=12)
run_time = easy_pace + 3*tempo_pace + easy_pace
end_time = start_time + run_time
print("3. Thời gian về nhà =", end_time.strftime("%H:%M:%S"))
