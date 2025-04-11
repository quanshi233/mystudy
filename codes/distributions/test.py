import numpy as np
import matplotlib.pyplot as plt
from math import comb  # 正确导入组合数函数
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows 系统

class X_B:
    def __init__(self, n, p):
        self.n = n
        self.p = p
        self.samples = np.random.binomial(n, p, 1000)  # 生成样本
        self.k = range(0, n+1)  # 所有可能成功次数
        # 计算理论PMF
        self.f = [comb(n, i) * (p**i) * ((1-p)**(n-i)) for i in self.k]

# 参数设置
n = 10
p = 0.5
a = X_B(n, p)  # 创建实例

# 绘图
plt.figure(figsize=(10, 6))
plt.hist(a.samples, 
         bins=np.arange(-0.5, n+1.5, 1), 
         density=True, 
         alpha=0.5, 
         label='样本分布')
plt.bar(a.k, a.f, 
        alpha=0.7, 
        color='red', 
        label='理论PMF')
plt.title(f'二项分布 (n={n}, p={p})')
plt.xlabel('成功次数')
plt.ylabel('概率')
plt.xticks(range(n+1))
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()