import numpy as np
import math
from scipy import stats

rng = np.random.default_rng(42)
mu = 10
sigma = 2
repeats = 10000
n_values = [5, 15, 50]

for n in n_values:
    # 改动1：t 临界值必须接住，并且提到内层循环外——它只依赖 n，不必重复算 1 万次
    t_crit = stats.t.ppf(0.975, df=n - 1)

    t_cover_count = 0
    total_width = 0

    # 改动2：循环下标改名为 _。原来的 i 只当计数器用，却被误当成标准误，用 _ 表明不参与计算
    for _ in range(repeats):
        samples = rng.normal(loc=mu, scale=sigma, size=n)
        x_bar = np.mean(samples)

        # 改动3：t_val 改名为 s。np.std(ddof=1) 算的是样本标准差，不是 t 值
        s = np.std(samples, ddof=1)

        # 改动4：原来的 se = i / sqrt(n) 用错了变量（i 是循环次数，不是标准差）。
        #         正确公式：边际误差 = t临界值 * s / sqrt(n)
        margin = t_crit * s / math.sqrt(n)
        down = x_bar - margin
        up = x_bar + margin

        # 改动5：改成链式比较，等价于 mu >= down and mu <= up
        if down <= mu <= up:
            t_cover_count += 1

        total_width += (up - down)

    # 改动6：原来只打印覆盖率，total_width 累加了却没用上，这里补上平均宽度
    print(f"n={n}: 覆盖率={t_cover_count / repeats:.4f}, 平均宽度={total_width / repeats:.4f}")