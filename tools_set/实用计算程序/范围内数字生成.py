import random


def generate_numbers(start, end, required_numbers, count, min_gap):
    # 先将要求的数字排序并放入列表中
    all_numbers = sorted(required_numbers)

    # 在要求的范围内生成候选数字
    candidate_numbers = []
    for num in range(start, end + 1):
        if num not in required_numbers:
            candidate_numbers.append(num)

    print(f"候选数字总数: {len(candidate_numbers)}")  # 输出候选数字的总数

    # 确保数字之间的间隔符合要求
    def can_add_number(num):
        for existing_num in all_numbers:
            if abs(existing_num - num) < min_gap:
                return False
        return True

    while len(all_numbers) < count:
        num = random.choice(candidate_numbers)
        if can_add_number(num):
            all_numbers.append(num)
            print(num)  # 逐个输出生成的数字

    # 返回最终排序的数字
    return sorted(all_numbers)


# 用户参数
required_numbers = {10, 21, 521, 666, 789, 1121}
num_count = 52
min_gap = 12

# 生成数字
result = generate_numbers(10, 1240, required_numbers, num_count, min_gap)

# 打印结果
print("最终生成的数字列表:", result)
