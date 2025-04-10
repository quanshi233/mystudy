def comb(self, n, k):
    """手写组合数计算函数"""
    if k < 0 or k > n:
        return 0
    # 优化计算顺序防止数值过大
    k = min(k, n - k)  # 利用对称性减少计算量
    result = 1
    for i in range(1, k+1):
        result = result * (n - i + 1) // i  # 使用整数除法避免浮点误差
    return result
