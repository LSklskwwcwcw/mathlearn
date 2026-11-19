import itertools
import numpy as np

def main():
    p = [2,4,6,8]
    N = len(p)


    samples =list(itertools.product(P,repeat=2))
    print(f"总体: {P}, 总体均值: {np.mean(P)}, 总体方差(ddof=0): {np.var(P)}")
    print(f"总共枚举出 {len(samples)} 组样本\n")

    print("--- 所有样本及方差明细 ---")
    print(f"{'样本':<10} | {'ddof=0 方差':<12} | {'ddof=1 方差':<12}")
    print("-" * 40)

    var_0_list = []
    var_1_list = []

    for s in samples:
        v0 = np.var(s,ddof=0)
        v1 = np.var(s,ddof=1)


        var_0_list.append(v0)
        var_1_list.append(v1)

        print(f"{str(s):<10} | {v0:<12.2f} | {v1:<12.2f}")



    mean_v0 = np.mean(var_0_list)
    mean_v1 = np.mean(var_1_list)
    
    print(f"\n--- 汇总对比 ---")
    print(f"ddof=0 方差的平均值: {mean_v0}")
    print(f"ddof=1 方差的平均值: {mean_v1}")
    print(f"总体真实方差: {np.var(P)}")
    
    if np.isclose(mean_v1, np.var(P)):
        print("\n结论: ddof=1 (无偏样本方差) 的平均值精确等于总体方差，而 ddof=0 是向下偏低的。")

if __name__ == "main":
    main()