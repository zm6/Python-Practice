#!/user/bin/env python
# -*- coding:utf-8 -*-
# 作者：zm6
# 创建：2021-03-19
# 更新：2021-03-19
# 用意：打印N以内的质数


import time  # 比较代码运行时间


def list_prime(n):
    num = 0

    for i in range(2, n + 1):
        is_prime = 1 #预设质数为是

        for j in range(2, i - 1):

            if i % j == 0:
                is_prime = 0 #设置质数为否
                break

        if is_prime == 1:
            print(i)
            num = num + 1
    return num


if __name__ == "__main__":
    n = int(input("please enter the number："))  # 输入n值
    start = time.time()  # 开始计时

    num = list_prime(n)
    print(n, "以内质数个数为：", num)

    end = time.time()  # 结束计时
    print(str(end - start))

