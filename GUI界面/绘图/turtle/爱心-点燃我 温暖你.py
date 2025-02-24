import random
from math import sin, cos, pi, log
from tkinter import *

# 定义画布尺寸和颜色
CANVAS_WIDTH = 640
CANVAS_HEIGHT = 480
CANVAS_CENTER_X = CANVAS_WIDTH / 2
CANVAS_CENTER_Y = CANVAS_HEIGHT / 2
IMAGE_ENLARGE_FACTOR = 11
HEART_COLOR = "#FF69B4"


def generate_heart_coordinate(t, shrink_ratio=IMAGE_ENLARGE_FACTOR):
    """
    生成爱心函数的坐标
    :param t: 参数，控制爱心的形状
    :param shrink_ratio: 爱心的缩放比例
    :return: 爱心的坐标 (x, y)
    """
    # 基础函数，生成爱心的基本形状
    x = 16 * (sin(t) ** 3)
    y = -(13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t))

    # 放大爱心
    x *= shrink_ratio
    y *= shrink_ratio

    # 将爱心移到画布中央
    x += CANVAS_CENTER_X
    y += CANVAS_CENTER_Y

    return int(x), int(y)


def scatter_inside(x, y, beta=0.15):
    """
    随机内部扩散，用于生成爱心内部的点
    :param x: 原点的 x 坐标
    :param y: 原点的 y 坐标
    :param beta: 扩散强度
    :return: 新点的坐标 (x, y)
    """
    ratio_x = - beta * log(random.random())
    ratio_y = - beta * log(random.random())

    dx = ratio_x * (x - CANVAS_CENTER_X)
    dy = ratio_y * (y - CANVAS_CENTER_Y)

    return x - dx, y - dy


def shrink_coordinate(x, y, ratio):
    """
    抖动效果，用于调整爱心的跳动
    :param x: 原点的 x 坐标
    :param y: 原点的 y 坐标
    :param ratio: 抖动的比例
    :return: 新点的坐标 (x, y)
    """
    force = -1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.6)  # 调整爱心跳动的参数
    dx = ratio * force * (x - CANVAS_CENTER_X)
    dy = ratio * force * (y - CANVAS_CENTER_Y)
    return x - dx, y - dy


def custom_curve(p):
    """
    自定义曲线函数，调整跳动周期
    :param p: 参数，控制曲线的形状
    :return: 正弦值，用于调整爱心的跳动
    """
    # 可以尝试换其他的动态函数，达到更有力量的效果（如贝塞尔曲线）
    return 2 * (2 * sin(4 * p)) / (2 * pi)


class BeatingHeart:
    """
    跳动的爱心类
    """

    def __init__(self, generate_frame=20):
        self._original_points = set()  # 原始爱心的坐标集合
        self._edge_diffusion_points = set()  # 边缘扩散效果的点坐标集合
        self._center_diffusion_points = set()  # 中心扩散效果的点坐标集合
        self.all_frame_points = {}  # 每帧的动态点坐标
        self.build(2000)

        self.random_halo = 1000

        self.generate_frame = generate_frame
        for frame in range(generate_frame):
            self.calculate_frame(frame)

    def build(self, number_of_points):
        # 生成原始爱心的坐标
        for _ in range(number_of_points):
            t = random.uniform(0, 2 * pi)  # 随机参数，用于生成不完整的爱心
            x, y = generate_heart_coordinate(t)
            self._original_points.add((x, y))

        # 生成爱心内扩散的点
        for x, y in list(self._original_points):
            for _ in range(3):
                x, y = scatter_inside(x, y, 0.05)
                self._edge_diffusion_points.add((x, y))

        # 生成爱心内再次扩散的点
        point_list = list(self._original_points)
        for _ in range(6000):
            x, y = random.choice(point_list)
            x, y = scatter_inside(x, y, 0.17)
            self._center_diffusion_points.add((x, y))

    @staticmethod
    def calculate_position(x, y, ratio):
        # 调整缩放比例
        force = 1 / (((x - CANVAS_CENTER_X) ** 2 + (y - CANVAS_CENTER_Y) ** 2) ** 0.520)  # 调整爱心跳动的参数

        dx = ratio * force * (x - CANVAS_CENTER_X) + random.randint(-1, 1)
        dy = ratio * force * (y - CANVAS_CENTER_Y) + random.randint(-1, 1)

        return x - dx, y - dy

    def calculate_frame(self, frame_number):
        ratio = 10 * custom_curve(frame_number / 10 * pi)  # 圆滑的周期的缩放比例

        halo_radius = int(4 + 6 * (1 + custom_curve(frame_number / 10 * pi)))
        halo_number = int(3000 + 4000 * abs(custom_curve(frame_number / 10 * pi) ** 2))

        all_points = []

        # 生成光环的点
        heart_halo_points = set()
        for _ in range(halo_number):
            t = random.uniform(0, 4 * pi)
            x, y = generate_heart_coordinate(t, shrink_ratio=11.5)
            x, y = shrink_coordinate(x, y, halo_radius)
            if (x, y) not in heart_halo_points:
                # 处理新的点
                heart_halo_points.add((x, y))
                x += random.randint(-14, 14)
                y += random.randint(-14, 14)
                size = random.choice((1, 2, 2))
                all_points.append((x, y, size))

        # 生成爱心轮廓的点
        for x, y in self._original_points:
            x, y = self.calculate_position(x, y, ratio)
            size = random.randint(1, 3)
            all_points.append((x, y, size))

        # 生成爱心内容的点
        for x, y in self._edge_diffusion_points:
            x, y = self.calculate_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        for x, y in self._center_diffusion_points:
            x, y = self.calculate_position(x, y, ratio)
            size = random.randint(1, 2)
            all_points.append((x, y, size))

        self.all_frame_points[frame_number] = all_points

    def render(self, render_canvas, render_frame):
        for x, y, size in self.all_frame_points[render_frame % self.generate_frame]:
            render_canvas.create_rectangle(x, y, x + size, y + size, width=0, fill=HEART_COLOR)


def draw(main_window, render_canvas, render_heart, render_frame=0):
    render_canvas.delete('all')
    render_heart.render(render_canvas, render_frame)
    main_window.after(160, draw, main_window, render_canvas, render_heart, render_frame + 1)


if __name__ == '__main__':
    root = Tk()
    root.title('Beating Heart')
    canvas = Canvas(root, bg='black', height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
    canvas.pack()
    heart = BeatingHeart()
    draw(root, canvas, heart)
    Label(root, text="stormsha", bg="black", fg="#FF69B4", ).place(relx=.5, rely=.5, anchor=CENTER)
    # 在爱心中间加上字
    Label(root, text="点燃我 温暖你", bg="black", fg="#FF69B4", font=('余生温柔都给你', 18)).place(relx=.50, rely=.1,
                                                                                         anchor=CENTER)
    # 在爱心上面加上字
    root.mainloop()
