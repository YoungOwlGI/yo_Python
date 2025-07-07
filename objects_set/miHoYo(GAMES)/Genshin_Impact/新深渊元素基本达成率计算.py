# data 的值是：当前元素已出角色数、我已有角色数，满足条件的角色数

data = {
    "火": [15, 12, 5],
    "水": [13, 11, 10],
    "风": [11, 9, 6],
    "雷": [13, 11, 4],
    "草": [10, 5, 4],
    "冰": [15, 12, 4],
    "岩": [11, 8, 4]
}

# 更新日期：2024年11月3日
print("新深渊——幻想真境剧诗 角色详情")

def calculate_achievement_rate(count1, count2):
    if count1 == 0:
        return 0.0
    return count2 / count1 * 100

from itertools import combinations

index = 1
for combo in combinations(data.keys(), 3):
    elements = list(combo)
    total_count_all = sum(data[element][0] for element in elements)
    total_count_mine = sum(data[element][1] for element in elements)
    total_count_satisfied = sum(data[element][2] for element in elements)
    achievement_rate_mine_all = calculate_achievement_rate(total_count_all, total_count_mine)
    achievement_rate_satisfied_mine = calculate_achievement_rate(total_count_mine, total_count_satisfied)
    print(f"{index}. {'+'.join(elements)}: 已出角色总数 {total_count_all}, 我的角色总数 {total_count_mine}, 符合要求角色总数 {total_count_satisfied}, 我的角色占已出角色百分比 {achievement_rate_mine_all:.2f}%, 符合要求角色占我的角色百分比 {achievement_rate_satisfied_mine:.2f}%")
    index += 1