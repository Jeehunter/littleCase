# 像素风格橡树绘制教程

使用Python和matplotlib库绘制橡树

## 项目概述

- 像素风格的橡树（树干和四层树叶）
- 天空背景和地面
- 远处的山丘
- 太阳

## 代码详解

### 1. 导入必要的库

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle, Circle, Polygon
```

- `matplotlib.pyplot`: 用于创建图形和绘图
- `numpy`: 用于数学运算和随机选择
- `matplotlib.patches`: 提供各种形状的绘制工具

### 2. 主函数：draw_pixel_style_oak_tree()

这是主要的绘图函数，负责创建整个场景。

#### 2.1 设置画布和背景

```python
fig, ax = plt.subplots(figsize=(8, 10))
ax.set_aspect('equal')
ax.set_facecolor('#87CEEB')
```

- `figsize=(8, 10)`: 设置图形大小为8x10英寸
- `set_aspect('equal')`: 保持x轴和y轴比例相等
- `set_facecolor('#87CEEB')`: 设置背景颜色为天空蓝

#### 2.2 绘制地面

```python
for x in range(20):
    for y in range(3):
        if (x + y) % 2 == 0:
            color = '#8B4513'
        else:
            color = '#A0522D'
        rect = Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black', linewidth=0.5)
        ax.add_patch(rect)
```

- 使用双循环创建20x3的地面网格
- 棋盘格效果：通过`(x + y) % 2`判断使用哪种棕色
- `Rectangle((x, y), 1, 1)`: 创建1x1的矩形方块

#### 2.3 绘制树干

```python
trunk_pixels = [
    (9, 3), (9, 4), (9, 5), (9, 6), (9, 7), (9, 8),
    (10, 3), (10, 4), (10, 5), (10, 6), (10, 7), (10, 8)
]
```

- 树干由12个方块组成，位置在x=9-10，y=3-8
- 使用深棕色`#8B4513`模拟木头颜色

#### 2.4 绘制树叶

树叶分为四层，从下到上宽度逐渐变窄：

##### 最底层树叶（y=7-10）
```python
# 最底层树叶（宽度最宽）
(5, 7), (6, 7), (7, 7), (8, 7), (9, 7), (10, 7), (11, 7), (12, 7), (13, 7), (14, 7),
(4, 8), (5, 8), (6, 8), (7, 8), (8, 8), (9, 8), (10, 8), (11, 8), (12, 8), (13, 8), (14, 8), (15, 8),
(5, 9), (6, 9), (7, 9), (8, 9), (9, 9), (10, 9), (11, 9), (12, 9), (13, 9), (14, 9),
(6, 10), (7, 10), (8, 10), (9, 10), (10, 10), (11, 10), (12, 10), (13, 10),
```

- 宽度最宽：从x=4到x=15
- 树干在中间位置可见

##### 底层树叶（y=11-14）
- 宽度适中，比最底层窄

##### 中层树叶（y=15-17）
- 宽度较窄

##### 顶层树叶（y=18-20）
- 宽度最窄

##### 树叶颜色随机化
```python
colors = ['#228B22', '#32CD32', '#006400']
color = np.random.choice(colors)
```

#### 2.5 绘制远处的山

```python
mountains = [
    # 左侧远处的山
    Polygon([(1, 3), (3, 6), (5, 3)], facecolor='#696969', edgecolor='#2F4F4F', linewidth=1),
    # 右侧远处的山
    Polygon([(14, 3), (16, 5), (18, 3)], facecolor='#696969', edgecolor='#2F4F4F', linewidth=1),
    # 更远处的山（更小）
    Polygon([(0, 3), (1, 4), (2, 3)], facecolor='#808080', edgecolor='#2F4F4F', linewidth=1),
    Polygon([(18, 3), (19, 4), (20, 3)], facecolor='#808080', edgecolor='#2F4F4F', linewidth=1),
]
```

- 使用`Polygon`类创建三角形山丘

#### 2.6 绘制太阳

```python
sun = Circle((17, 17), 2, facecolor='#FFD700', edgecolor='#FFA500', linewidth=2)
```

- 位置在右上角(x=17, y=17)
- 使用金色`#FFD700`和橙色边框`#FFA500`

#### 2.7 设置坐标轴和显示

```python
ax.set_xlim(0, 20)
ax.set_ylim(0, 22)
ax.set_xticks([])
ax.set_yticks([])
plt.title('像素风格橡树', fontsize=16, fontfamily='SimHei')
plt.tight_layout()
plt.show()
```

- `set_xlim`和`set_ylim`: 设置坐标轴范围
- `set_xticks([])`和`set_yticks([])`: 隐藏坐标轴刻度
- `title`: 设置图形标题
- `tight_layout()`: 自动调整布局
- `show()`: 显示图形

### 3. 运行程序

```python
if __name__ == "__main__":
    print("正在绘制像素风格橡树...")
    draw_pixel_style_oak_tree()
```

## 运行方法

1. 确保安装了必要的库：
```bash
pip install matplotlib numpy
```

2. 运行程序：
```bash
python minecraft_oak_tree.py
```


## 颜色参考

- 天空蓝: `#87CEEB`
- 树干棕: `#8B4513`
- 地面棕: `#8B4513`, `#A0522D`
- 树叶绿: `#228B22`, `#32CD32`, `#006400`
- 太阳金: `#FFD700`, `#FFA500`
- 山丘灰: `#696969`, `#808080`
