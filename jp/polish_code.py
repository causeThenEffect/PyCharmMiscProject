# python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter
from typing import Tuple, List, Optional

# 全局字体设置（保持原有中文字体）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = ['Heiti TC']
plt.rcParams['axes.unicode_minus'] = False


def format_thousands(x, pos=None) -> str:
    """将数字格式化为千分位字符串（整数）用于刻度和注释。"""
    return f"{int(x):,}"


def compute_investment(monthly_invest: float, annual_rate: float, years: int) -> Tuple[List[float], List[float], List[float]]:
    """
    计算每月累计本金、账户余额与利息（含复利）。
    返回 (balances, principals, interests) 三个列表，长度 = years * 12
    """
    months = years * 12
    monthly_rate = annual_rate / 12.0

    balance = 0.0
    balances = []
    principals = []

    for m in range(1, months + 1):
        balance = balance * (1 + monthly_rate) + monthly_invest
        balances.append(balance)
        principals.append(monthly_invest * m)

    interests = [b - p for b, p in zip(balances, principals)]
    return balances, principals, interests


def aggregate_yearly(values: List[float], years: int) -> List[float]:
    """按年（每 12 个月的最后一个月）汇总时间序列数据。"""
    return [values[(i + 1) * 12 - 1] for i in range(years)]


def plot_investment(
    monthly_invest: float = 1000,
    annual_rate: float = 0.07,
    years: int = 35,
    figsize: Tuple[int, int] = (12, 6),
    save_path: Optional[str] = None
) -> None:
    """计算并绘制每月定投复利增长的堆叠柱状图和总额折线图。"""
    balances, principals, interests = compute_investment(monthly_invest, annual_rate, years)

    year_labels = np.arange(1, years + 1)
    principals_y = aggregate_yearly(principals, years)
    balances_y = aggregate_yearly(balances, years)
    interests_y = aggregate_yearly(interests, years)

    fig, ax = plt.subplots(figsize=figsize)
    ax.bar(year_labels, principals_y, label="累计本金", color='skyblue')
    ax.bar(year_labels, interests_y, bottom=principals_y, label="利息收益（含复利）", color='orange', alpha=0.8)
    ax.plot(year_labels, balances_y, label="账户总额（复利）", color='green', linewidth=2, marker='o')

    # 千分位刻度格式与轴标签
    ax.yaxis.set_major_formatter(FuncFormatter(format_thousands))
    ax.set_xlabel("年份")
    ax.set_ylabel("金额（元）")
    ax.set_title(f"每月定投 {int(monthly_invest):,} 元，年化 {annual_rate*100:.2f}%，{years} 年（柱状图 + 折线）")

    # 动态 y 轴上限：稍大于最终余额，保证注释不被切掉
    ymax = balances_y[-1] * 1.12
    ax.set_ylim(0, ymax)

    # 在柱状顶部标注每年利息（千分位）
    text_offset = ymax * 0.02
    for x, total, interest in zip(year_labels, balances_y, interests_y):
        ax.text(x, total + text_offset, format_thousands(interest), ha='center', va='bottom', color='red', fontsize=9)

    ax.set_xticks(year_labels)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend()
    plt.tight_layout()

    if save_path:
        fig.savefig(save_path, dpi=300)
    plt.show()


if __name__ == "__main__":
    # 示例调用：使用原始参数
    plot_investment(monthly_invest=1000, annual_rate=0.07, years=35, save_path=None)