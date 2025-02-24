from datetime import datetime, timedelta

# 设定未来时间
future_time_str = "2025-01-14 08:00:00"
future_time = datetime.strptime(future_time_str, "%Y-%m-%d %H:%M:%S")

# 获取当前时间
current_time = datetime.now()

# 计算时间差
time_difference = future_time - current_time

# 将时间差转换为秒、分钟和小时
seconds_left = time_difference.total_seconds()
minutes_left = int(seconds_left / 60)
hours_left = int(minutes_left / 60)

# 输出结果
print(f"距离 {future_time_str} （计算机二级考试）还剩：")
print(f"秒数：{int(seconds_left)}")
print(f"分钟数：{minutes_left}")
print(f"小时数：{hours_left}")

# 如果你想得到剩余的天数，也可以这样计算
days_left = int(hours_left / 24)
hours_left %= 24  # 剩余的小时数（不足一天的部分）
print(f"天数：{days_left}")