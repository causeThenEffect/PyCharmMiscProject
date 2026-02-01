import matplotlib.pyplot as plt
import numpy as np

# 数据
feedback_types = ['AI Feedback', 'Teacher Feedback']
stages = ['Pretest', 'Midtest', 'Posttest']

# 分数：行对应阶段，列对应反馈类型
scores = np.array([
    [60, 65],  # Pretest: AI, Teacher
    [80, 78],  # Midtest
    [88, 85]   # Posttest
])

# 设置柱状图位置
x = np.arange(len(feedback_types))  # x轴位置
width = 0.2  # 每根柱子的宽度

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制每个阶段的柱子
for i, stage in enumerate(stages):
    ax.bar(x + i*width - width, scores[i], width, label=stage)

# 设置横轴、纵轴标签和标题
# ax.set_xlabel('Feedback Type')
ax.set_ylabel('speaking score')
ax.set_title('')
ax.set_xticks(x)
ax.set_xticklabels(feedback_types)
plt.title("overall speaking performance gains")

ax.legend(title='Test Stage')

# 显示图形
plt.tight_layout()
plt.show()
