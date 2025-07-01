import cv2
import os
import glob
import numpy as np

# 强化版配置参数
CONFIG = {
    "input_dir": "./frame",
    "output_dir": "./masked_frame_enhanced",
    "red_detection": {
        "hsv_ranges": [
            {"lower": [0, 50, 50], "upper": [10, 255, 255]},  # 扩展红色检测范围
            {"lower": [160, 50, 50], "upper": [180, 255, 255]}
        ],
        "morph_kernel": (7, 7),  # 增大形态学核尺寸
        "morph_iterations": 3  # 增加形态学操作次数
    },
    "roi_settings": {
        "x_range": (0.6, 1.0),  # 扩大右侧处理范围
        "y_range": (0.0, 0.4)  # 覆盖更多垂直区域
    },
    "mosaic": {
        "intensity": 25,  # 增强马赛克力度
        "expand": {"x": 15, "y": 10}  # 增加扩展像素
    }
}


def enhance_red_detection(hsv_img):
    """强化红色检测"""
    masks = []
    for range in CONFIG["red_detection"]["hsv_ranges"]:
        lower = np.array(range["lower"])
        upper = np.array(range["upper"])
        masks.append(cv2.inRange(hsv_img, lower, upper))

    combined_mask = cv2.bitwise_or(masks[0], masks[1])

    # 强化形态学处理
    kernel = cv2.getStructuringElement(
        cv2.MORPH_ELLIPSE,
        CONFIG["red_detection"]["morph_kernel"]
    )
    return cv2.morphologyEx(
        combined_mask,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=CONFIG["red_detection"]["morph_iterations"]
    )


def get_roi_coordinates(img_shape):
    """获取处理区域坐标"""
    h, w = img_shape[:2]
    return (
        int(w * CONFIG["roi_settings"]["x_range"][0]),  # x_start
        int(h * CONFIG["roi_settings"]["y_range"][0]),  # y_start
        int(w * CONFIG["roi_settings"]["x_range"][1]),  # x_end
        int(h * CONFIG["roi_settings"]["y_range"][1])  # y_end
    )


def apply_aggressive_mosaic(region):
    """应用强力马赛克（添加尺寸校验）"""
    h, w = region.shape[:2]

    # 确保最小尺寸
    intensity = max(1, CONFIG["mosaic"]["intensity"])
    new_w = max(1, w // intensity)
    new_h = max(1, h // intensity)

    # 双重马赛克处理
    small = cv2.resize(region, (new_w, new_h))
    mosaic = cv2.resize(small, (w, h), interpolation=cv2.INTER_NEAREST)

    # 添加安全校验
    if mosaic.shape != region.shape:
        mosaic = cv2.resize(mosaic, (w, h))

    return cv2.GaussianBlur(mosaic, (5, 5), 0)


def process_image(img):
    """强化处理流程（修复轮廓检测问题）"""
    # 获取处理区域
    x1, y1, x2, y2 = get_roi_coordinates(img.shape)

    # 校验区域有效性
    if x1 >= x2 or y1 >= y2:
        print(f"警告：无效处理区域 {x1}-{x2}, {y1}-{y2}")
        return img

    roi = img[y1:y2, x1:x2]

    # 红色检测强化
    hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    mask = enhance_red_detection(hsv)

    # 正确获取轮廓
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 修复此处

    # 查找并扩展区域
    for cnt in contours:
        if cv2.contourArea(cnt) < 50:
            continue

        # 获取边界框并扩展
        x, y, w, h = cv2.boundingRect(cnt)
        exp_x = CONFIG["mosaic"]["expand"]["x"]
        exp_y = CONFIG["mosaic"]["expand"]["y"]

        # 转换为原图坐标
        abs_x = x1 + max(0, x - exp_x)
        abs_y = y1 + max(0, y - exp_y)
        abs_x2 = x1 + min(x2 - x1, x + w + exp_x)
        abs_y2 = y1 + min(y2 - y1, y + h + exp_y)

        # 跳过无效区域
        if abs_x2 <= abs_x or abs_y2 <= abs_y:
            continue

        # 应用强力马赛克
        try:
            img[abs_y:abs_y2, abs_x:abs_x2] = apply_aggressive_mosaic(
                img[abs_y:abs_y2, abs_x:abs_x2]
            )
        except Exception as e:
            print(f"处理异常区域：{abs_x}-{abs_x2}, {abs_y}-{abs_y2} 错误：{str(e)}")

    return img

def batch_processing():
    os.makedirs(CONFIG["output_dir"], exist_ok=True)

    for img_file in glob.glob(os.path.join(CONFIG["input_dir"], "*.*")):
        if not img_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            continue

        img = cv2.imread(img_file)
        if img is None:
            continue

        processed = process_image(img)
        cv2.imwrite(os.path.join(CONFIG["output_dir"],
                                 os.path.basename(img_file)), processed)


if __name__ == "__main__":
    print("强化版处理参数：")
    print(f"检测范围：右侧 {CONFIG['roi_settings']['x_range'][0] * 100}%~100%")
    print(f"马赛克强度：{CONFIG['mosaic']['intensity']} 级")
    print(f"区域扩展：横向 {CONFIG['mosaic']['expand']['x']}px, 纵向 {CONFIG['mosaic']['expand']['y']}px")

    batch_processing()
    print(f"处理完成！结果保存在：{os.path.abspath(CONFIG['output_dir'])}")