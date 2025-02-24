import tkinter as yzy
from tkinter import font  # 确保导入了 font 子模块
import random
#导入包
import webbrowser



def xh():
    root.destroy()
def dkwy():#定义访问路径
    url = "http://love.sakura.gold"
    ##执行包命令打开指定网页
    webbrowser.open(url, new=0, autoraise=True)

root = yzy.Tk()
root.title("Love-樱振宇")
# 获取屏幕分辨率
idth = root.winfo_screenwidth()
eight = root.winfo_screenheight()
x=int(idth/2)-150
y=int(eight/2)-100
root.geometry(f"300x200+{x}+{y}")
zynr="如果你喜欢一个人，就要勇敢的表白，不要怕被拒绝，因为被拒绝没什么，至少你已经努力了。"
link = yzy.Label(root,font=font.Font(size=16,weight='bold'),wraplength=280, text=zynr).pack()
button = yzy.Button(root, text="这就去表白！", command=dkwy).pack()
button = yzy.Button(root, text="还是再见吧！", command=xh).pack()
love_bq = [
    "和你在一起只是我不想给任何人机会。",
    "请你当我手心里的宝。",
    "如果有幸福，我让它有声有色地蔓延!",
    "假如我变成黄土，黄土也爱着你;假如黄土上长满青草，青草也爱着你;假如青草上挂满露珠，露珠也爱着你。",
    "好笑吗 身边没你，好怪，陪我一生一世好吗?",
    "这辈子没缘，下辈子一定要投胎在一起。",
    "玫瑰开在九月里，我的心中只有你，好想和你在一起，没有什么送给你，只有一句我爱你!",
    "我爱月，爱它纯，爱它明，爱它圆。我爱你，爱你真，爱你善，爱你美。",
    "如果有幸福，我让它有声有色地蔓延! 如果有忧伤，我把它无声无息地吹散。",
    "假如你是我梦中那只收桅待泊的船，我愿是那静静的湾，荡着轻柔的浪，舒展着迷人的滩。",
    "他的幸福里没有我的位置我的幸福里只有他。",
    "我想要一个拥抱，但是你的拥抱或许永远也不属于我。",
    "如果有幸福，我让它有声有色地蔓延!",
    "我是加油的小废物樱振宇！",
    "不知道爱你算不算是一个贴心的理由",
    "做不了你的影子，就让我做一阵风萦绕在你的身边。",
    "梦见你忘却疲惫，想你想得无法入睡，别说你还无所谓，收下我的红玫瑰，你不爱我是你不对!",
    "我们太善良连自己都骗不过我爱你说未来很长一切难讲。",
    "如果有忧伤，我把它无声无息地吹散。",
    "宝贝吾爱，我的心与你同在;你的心跳连着我的血脉，你的步伐是我生命的节拍;即使所有的都化作尘埃，我也永不言败 。",
    "不知道爱你算不算是一个贴心的理由?",
    "我想要和你一起慢慢变老。",
    "我不是你想去的地方爱越拉扯越疼痛不再抢救。",
    "宝贝吾爱，我的心与你同在;你的心跳连着我的血脉，你的步伐是我生命的节拍;即使所有的都化作尘埃，我也永不言败。",
    "做不了你的太阳，就让我做你的影子。",
    "我们太善良 连自己 都骗不过 我爱 你说未来很长 一切难讲。",
    "我不是你 想去的地方 爱越拉扯越疼痛 不再抢救。",
    "我不是你的花，你的鲜艳都属于别人；我不是你的书，你的精彩全归别人。所以，请你不要对我有任何的期盼。",
    "你是最可爱的，也是最让我心动的！我想和你在一起，无论今后的路有多难走，风雨坎坷！",
    "我不怕你是一只绵羊，也不怕你是一只灰狼；我不怕你是一片大海，也不怕你是一潭死水。我最怕的是，我们连彼此的心都猜忌！",
    "我不想让你孤单，所以特地给自己添了一个最爱的朋友；我不想让你孤单，所以特地为你建造了最美的花园。愿你在花园里尽情开放，在爱人身旁自由飞翔！",
    "我喜欢你，就像小鸟一样，在头上筑巢，等着每一个食客的到来。",
    "你是我的最爱，我愿意等你一生。",
    "如果你喜欢一个人，就要勇敢的表白，不要怕被拒绝，因为被拒绝没什么，至少你已经努力了。"
]

def generate_random_color():
    # 生成一个随机的十六进制颜色代码
    # '#%02X%02X%02X' 是格式化字符串，用于将三个0到255之间的随机整数转换为六位十六进制数
    return '#%02X%02X%02X' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def love():
    for i in range(6):
        for i in range(len(love_bq)):
            toplevel = yzy.Toplevel(root)
            toplevel.title("love.sakura.gold")
            #color
            ys_color=generate_random_color()
            toplevel.configure(bg= ys_color)
            label_font = font.Font(size=16,weight='bold')
            yzy.Label(toplevel, text=love_bq[i],bg=ys_color,font=label_font,wraplength=280,fg="white").pack()
            x=random.randint(0, idth-300)
            y=random.randint(0, eight-200)
            toplevel.geometry(f"300x200+{x}+{y}")
            #print(toplevel.winfo_width())

#for sz in range(10):
love()

root.mainloop()