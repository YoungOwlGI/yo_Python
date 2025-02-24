import datetime
import tkinter as tk
from tkinter import messagebox


def calculate_draws():
    # 创建主窗口
    root = tk.Tk()
    root.title("抽卡计算器")
    root.geometry("300x400")

    # 存储输入框和复选框的变量
    input_vars = []
    checkbox_vars = []

    # 输入框1和复选框1
    label1 = tk.Label(root, text="请输入原石数量：")
    label1.grid(row=0, column=0, padx=10, pady=5, sticky='w')

    input_var1 = tk.StringVar()
    input_entry1 = tk.Entry(root, textvariable=input_var1, width=10)
    input_entry1.grid(row=0, column=1, padx=10, pady=5)

    checkbox_var1 = tk.BooleanVar()
    input_checkbox1 = tk.Checkbutton(root, variable=checkbox_var1)
    input_checkbox1.grid(row=0, column=2, padx=10, pady=5)

    input_vars.append(input_var1)
    checkbox_vars.append(checkbox_var1)

    # 输入框2和复选框2
    label2 = tk.Label(root, text="请输入纠缠之缘数量：")
    label2.grid(row=1, column=0, padx=10, pady=5, sticky='w')

    input_var2 = tk.StringVar()
    input_entry2 = tk.Entry(root, textvariable=input_var2, width=10)
    input_entry2.grid(row=1, column=1, padx=10, pady=5)

    checkbox_var2 = tk.BooleanVar()
    input_checkbox2 = tk.Checkbutton(root, variable=checkbox_var2)
    input_checkbox2.grid(row=1, column=2, padx=10, pady=5)

    input_vars.append(input_var2)
    checkbox_vars.append(checkbox_var2)

    # 输入框3和复选框3
    label3 = tk.Label(root, text="请输入星辉数量：")
    label3.grid(row=2, column=0, padx=10, pady=5, sticky='w')

    input_var3 = tk.StringVar()
    input_entry3 = tk.Entry(root, textvariable=input_var3, width=10)
    input_entry3.grid(row=2, column=1, padx=10, pady=5)

    checkbox_var3 = tk.BooleanVar()
    input_checkbox3 = tk.Checkbutton(root, variable=checkbox_var3)
    input_checkbox3.grid(row=2, column=2, padx=10, pady=5)

    input_vars.append(input_var3)
    checkbox_vars.append(checkbox_var3)

    # 输入框4和复选框4
    label4 = tk.Label(root, text="请输入垫的数量：")
    label4.grid(row=3, column=0, padx=10, pady=5, sticky='w')

    input_var4 = tk.StringVar()
    input_entry4 = tk.Entry(root, textvariable=input_var4, width=10)
    input_entry4.grid(row=3, column=1, padx=10, pady=5)

    checkbox_var4 = tk.BooleanVar()
    input_checkbox4 = tk.Checkbutton(root, variable=checkbox_var4)
    input_checkbox4.grid(row=3, column=2, padx=10, pady=5)

    input_vars.append(input_var4)
    checkbox_vars.append(checkbox_var4)

    # 输入框5和复选框5
    label5 = tk.Label(root, text="请输入创世结晶数量：")
    label5.grid(row=4, column=0, padx=10, pady=5, sticky='w')

    input_var5 = tk.StringVar()
    input_entry5 = tk.Entry(root, textvariable=input_var5, width=10)
    input_entry5.grid(row=4, column=1, padx=10, pady=5)

    checkbox_var5 = tk.BooleanVar()
    input_checkbox5 = tk.Checkbutton(root, variable=checkbox_var5)
    input_checkbox5.grid(row=4, column=2, padx=10, pady=5)

    input_vars.append(input_var5)
    checkbox_vars.append(checkbox_var5)

    # 计算按钮
    calculate_button = tk.Button(root, text="计算", command=lambda: calculate_sum(input_vars, checkbox_vars))
    calculate_button.grid(row=5, column=0, columnspan=3, pady=20)

    # 显示结果的标签
    result_label = tk.Label(root, text="目前抽数: ")
    result_label.grid(row=6, column=0, columnspan=3, pady=10)

    def calculate_sum(input_vars, checkbox_vars):
        try:
            sum_value = 0
            # 处理输入框1和5的值，分别除以160
            value1 = float(input_var1.get()) / 160 if checkbox_var1.get() else 0
            value5 = float(input_var5.get()) / 160 if checkbox_var5.get() else 0

            # 处理输入框3的值，除以5（退一法）
            value3 = int(float(input_var3.get()) / 5) if checkbox_var3.get() else 0

            # 累加其他框的值
            value2 = float(input_var2.get()) if checkbox_var2.get() else 0
            value4 = float(input_var4.get()) if checkbox_var4.get() else 0

            # 计算总和
            sum_value = value1 + value2 + value3 + value4 + value5
            result_label.config(text=f"目前抽数: {sum_value}")
        except ValueError:
            messagebox.showerror("输入错误", "请输入有效的数字")

    # 运行主循环
    root.mainloop()


def genshin_import():
    print("可选选项：\n")
    judgement_gi = input("请输入 调试方向：")
    if judgement_gi in ["抽卡计算","cd"]:
        calculate_draws()
    elif judgement_gi == "dc_1":
        pass
    else:
        pass


def star_rail():
    pass


def zenless_zone_zero():
    pass


def honkai_import_3():
    def level_3_7_8():
        end = 80000
        now = int(input("请输入当前值："))
        difference = end - now
        print("目前的差值是：", difference)
        """
            rice = 水稻
            wheat = 小麦
            frequency = 次数
            amount = 金额
            physical = 体力
            sow = 播种
            watering = 浇水
            harvest = 收割
        """
        # 售价
        rice_amount = 700
        wheat_amount = 400
        star_tomato_amount = 40
        # 体力消耗
        physical_sow = 1
        physical_watering = physical_harvest = 9

        rice_frequency = difference / rice_amount
        print("只种水稻需要种", rice_frequency, "个。")
        physical_r_f = rice_frequency * (physical_sow + physical_watering + physical_harvest)
        print("纯计算所得体力结果：", physical_r_f)

        def rice_phy():
            over_sow = int(input("请输入已播种水稻："))
            over_watering = int(input("请输入已浇水水稻："))
            # 计算已播种的水稻还需要多少体力
            sowed: int = over_sow * (physical_watering + physical_harvest)
            # print(sowed)
            # 计算已浇水的水稻还需要多少体力
            watered: int = over_watering * physical_harvest
            # print(watered)
            # # 计算意外值体力之和
            # num = sowed + watered

            end_num_all = rice_frequency - (over_sow + over_watering)
            end_num_all_product = end_num_all * (physical_sow + physical_watering + physical_harvest)
            end_num = end_num_all_product + sowed + watered
            print("需要体力：", end_num)
            # 计算所需体力
            print("\n下一步准备调试时间函数程序正确性：\n")

            def time_honkai3():
                now_physical = int(input("当前体力："))
                time_1 = 90
                # reverse 反向   计算的是精确的还需要的体力值
                now_physical_reverse = end_num - now_physical
                physical_seconds = now_physical_reverse * time_1
                # 体力刷新需要时间（秒）
                print("体力刷新所需秒：", physical_seconds)
                print("体力刷新所需分钟：", physical_seconds / 60)
                print("体力刷新所需小时：", physical_seconds / 3600)
                # 获取当前时间
                current_time = datetime.datetime.now()
                # 计算下一次体力刷新时间
                next_refresh_time = current_time + datetime.timedelta(seconds=physical_seconds)
                # 计算距离下次刷新体力的时间差
                time_difference = next_refresh_time - current_time
                print(f"距离体力满足要求还有 {time_difference}。")
                print(f"体力将在{next_refresh_time}满足要求。")

            time_honkai3()

        judgement_hi = input("是否要继续调试程序（是y否n）：")
        if judgement_hi == "y":
            rice_phy()
        elif judgement_hi == "n":
            pass
        else:
            print("请正确输入！")

    def level_4_7_8():
        def fishing():
            num_all = 10
            num = int(input("请输入钓鱼次数："))
            physical_fish = (num_all - num) * 45
            print("钓鱼需要的体力：", physical_fish)
            # 计算鱼饵需要的时间
            time_1 = 90
            fish_seconds = physical_fish * time_1
            print("鱼饵需要的时间：", fish_seconds)
            # 计算距离下次刷新体力的时间差
            current_time = datetime.datetime.now()
            next_refresh_time = current_time + datetime.timedelta(seconds=fish_seconds)
            time_difference = next_refresh_time - current_time
            print(f"距离体力满足要求还有 {time_difference}。")
            print(f"体力将在{next_refresh_time}满足要求。")

        fishing()

        def mining():
            num_all = 15
            num = int(input("请输入挖矿次数："))
            physical_mine = (num_all - num) * 9
            print("挖矿需要的体力：", physical_mine)
            # 计算矿石需要的时间
            time_1 = 90
            mine_seconds = physical_mine * time_1
            print("矿石需要的时间：", mine_seconds)
            # 计算距离下次刷新体力的时间差
            current_time = datetime.datetime.now()
            next_refresh_time = current_time + datetime.timedelta(seconds=mine_seconds)
            time_difference = next_refresh_time - current_time
            print(f"距离体力满足要求还有 {time_difference}。")
            print(f"体力将在{next_refresh_time}满足要求。")

        mining()
    judgement_level = input("请输入需要计算的游戏模块：")
    if judgement_level == "3-7-8":
        level_3_7_8()
    elif judgement_level == "4-7-8":
        level_4_7_8()
    else:
        print("请正确输入！")

def l():
    games = {
        genshin_import:["原神","genshin","GI","genshin impact"],
        honkai_import_3:["崩坏3","honkai","HI3","honkai 3rd"],
        zenless_zone_zero:["绝区零","ZZZ","ZZZ","zero zero zero"],
        star_rail:["崩坏：星穹铁道","star rail","SR","star rail"]
    }
    for func, values in games.items():
        print(f"※ 函数名：{func.__name__}，对应游戏名：{values}")

def main():
    judgement = input("请输入需要计算测试的游戏（不清楚如何输入请输入 l）：")
    if judgement == "l":
        l()
    elif judgement in ["原神","genshin","GI","genshin impact"]:
        genshin_import()
    elif judgement in ["崩坏3","honkai","HI3","honkai 3rd"]:
        honkai_import_3()
    elif judgement in ["绝区零","ZZZ","ZZZ","zero zero zero"]:
        zenless_zone_zero()
    elif judgement in ["崩坏：星穹铁道","star rail","SR","star rail"]:
        star_rail()
    else:
        print("输入的游戏未找到对应计算函数。以下是可选游戏：")
        l()


if __name__ == '__main__':
    main()
