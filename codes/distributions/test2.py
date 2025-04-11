import numpy as np
import matplotlib.pyplot as plt
from math import comb
class X_B:
    def __init__(self,n,p):
        samples = np.random.binomial(n, p, 1000)
        self.samples = samples
        self.k = range(0,n+1)
        self.f = [comb(n,i)*(p**(i))*((1-p)**(n-i)) for i in self.k]
n = 30
p = 0.5
a = X_B(n,p)
plt.figure(figsize=(10, 6))
plt.subplot(1,2,1)
plt.hist(a.samples, bins=np.arange(-0.5, n+1.5, 1), density=True, alpha=0.5, label='样本分布')
plt.subplot(1,2,2)
plt.bar(a.k, a.f, alpha=0.7, label='theoratical PMF')
plt.title(f'binomial distribution (n={n}, p={p})')
plt.xlabel('times of success')
plt.ylabel('probability')
plt.xticks(range(n+1))               # 设置x轴刻度为0~10
plt.legend()  # 显示图例
plt.grid(True, linestyle='--', alpha=0.5)  # 添加虚线网格
plt.show()
