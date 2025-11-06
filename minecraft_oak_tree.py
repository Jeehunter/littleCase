import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon

def draw_pixel_style_oak_tree():
    """绘制像素风格的橡树"""
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_aspect('equal')
    
    # 设置背景
    ax.set_facecolor('#87CEEB')
    
    # 绘制地面（像素风格）
    for x in range(20):
        for y in range(3):
            if (x + y) % 2 == 0:
                color = '#8B4513'
            else:
                color = '#A0522D'
            rect = Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black', linewidth=0.5)
            ax.add_patch(rect)
    
    # 绘制树干（像素风格）
    trunk_pixels = [
        (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
        (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8)
    ]
    
    for x, y in trunk_pixels:
        rect = Rectangle((x, y), 1, 1, facecolor='#8B4513', edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
    
    # 绘制树叶（像素风格）
    leaves_pixels = [
        # 最底层树叶
        (5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7),
        (4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8),
        (5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
        (6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10),
        
        # 底层树叶
        (7, 11), (8, 11), (9, 11), (10, 11), (11, 11), (12, 11),
        (6, 12), (7, 12), (8, 12), (9, 12), (10, 12), (11, 12), (12, 12), (13, 12),
        (7, 13), (8, 13), (9, 13), (10, 13), (11, 13), (12, 13),
        (8, 14), (9, 14), (10, 14), (11, 14),
        
        # 中层树叶
        (8, 15), (9, 15), (10, 15), (11, 15),
        (7, 16), (8, 16), (9, 16), (10, 16), (11, 16), (12, 16),
        (8, 17), (9, 17), (10, 17), (11, 17),
        
        # 顶层树叶
        (9, 18), (10, 18),
        (8, 19), (9, 19), (10, 19), (11, 19),
        (9, 20), (10, 20)
    ]
    
    for x, y in leaves_pixels:
        # 随机选择树叶颜色
        colors = ['#228B22', '#32CD32', '#006400']
        color = np.random.choice(colors)
        rect = Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
    
    # 绘制远处的山（三角形图案）
    mountains = [
        # 左侧远处的山
        Polygon([(1, 3), (3, 6), (5, 3)], facecolor='#696969', edgecolor='#2F4F4F', linewidth=1),
        # 右侧远处的山
        Polygon([(14, 3), (16, 5), (18, 3)], facecolor='#696969', edgecolor='#2F4F4F', linewidth=1),
        # 更远处的山
        Polygon([(0, 3), (1, 4), (2, 3)], facecolor='#808080', edgecolor='#2F4F4F', linewidth=1),
        Polygon([(18, 3), (19, 4), (20, 3)], facecolor='#808080', edgecolor='#2F4F4F', linewidth=1),
    ]
    
    for mountain in mountains:
        ax.add_patch(mountain)
    
    # 绘制太阳
    sun = Circle((17, 17), 2, facecolor='#FFD700', edgecolor='#FFA500', linewidth=2)
    ax.add_patch(sun)
    
    # 设置坐标轴范围
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 22)
    
    # 隐藏坐标轴
    ax.set_xticks([])
    ax.set_yticks([])
    
    # 添加标题
    plt.title('像素风格橡树', fontsize=16, fontfamily='SimHei')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("正在绘制像素风格橡树...")
    draw_pixel_style_oak_tree()
