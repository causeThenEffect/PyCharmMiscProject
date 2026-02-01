import matplotlib.pyplot as plt

# 定义维度和分数
categories = ["fluency", "accuracy", "pronunciation", "complexity"]
ai_scores = [85, 75, 80, 88]       # AI 分数
teacher_scores = [65, 60, 70, 68]  # teacher 分数低于 AI

# 设置横坐标位置
x = range(len(categories))

# 绘制柱状图
plt.bar([i + 0.15 for i in x], ai_scores, width=0.3, label="AI Feedback", color='skyblue')
plt.bar([i - 0.15 for i in x], teacher_scores, width=0.3, label="Teacher Feedback", color='salmon')

# 添加标签和标题
plt.xticks(x, categories)
plt.ylabel("gain score")
plt.ylim(0, 100)
plt.title("speaking gains across dimensions")
plt.legend()

# 显示图表
plt.show()


