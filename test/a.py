# ==========================
# 1️⃣ 导入库
# ==========================
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False


# ==========================
# 2️⃣ 创建数据
# ==========================
years = list(range(2015, 2025))
divorces = [384.14, 415.82, 437.40, 446.08, 470.06, 433.90, 283.93, 287.92, 360.53, 351.30]  # 万对

df = pd.DataFrame({
    "年份": years,
    "离婚登记人数（万对）": divorces
})

# ==========================
# 3️⃣ 显示表格
# ==========================
# 直接渲染漂亮表格
df.style.format({"离婚登记人数（万对）": "{:.2f}"})

# ==========================
# 4️⃣ 绘制趋势图
# ==========================
plt.figure(figsize=(10,6))
plt.plot(df["年份"], df["离婚登记人数（万对）"], marker='o', linestyle='-', color='red')
plt.title("中国近十年离婚人数趋势（2015-2024）", fontsize=14)
plt.xlabel("年份", fontsize=12)
plt.ylabel("离婚登记人数（万对）", fontsize=12)
plt.xticks(years)
plt.grid(True, linestyle='--', alpha=0.6)
plt.ylim(250, 500)

# 标注每个数据点
for x, y in zip(df["年份"], df["离婚登记人数（万对）"]):
    plt.text(x, y+5, f"{y:.0f}", ha='center', fontsize=10)

plt.show()
