import matplotlib.pyplot as plt
import numpy as np

# 数据
feedback_types = ['AI Feedback', 'Teacher Feedback']
stages = ['Pretest', 'Midtest', 'Posttest']

# 分数：行对应阶段，列对应反馈类型
scores = np.array([
    [60, 60],  # Pretest: AI > Teacher
    [85, 73],  # Midtest
    [92, 82]   # Posttest
])

# 设置柱子宽度
width = 0.2
x = np.arange(len(feedback_types))

# 绘制每个阶段的柱子
for i, stage in enumerate(stages):
    plt.bar(x + i*width - width, scores[i], width, label=stage)

# 设置标签和标题
# plt.xlabel('Feedback Type')
plt.ylabel('speaking score')
plt.title('overall speaking performance gains')
plt.xticks(x, feedback_types)
plt.ylim(0, 100)  # 设置纵轴分数最高为100
plt.legend(loc='upper left')  # 图例显示在左上角

plt.tight_layout()
plt.show()
