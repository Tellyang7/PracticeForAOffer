"""
输入描述：

1、忽略小数点，例如“A1.2”，认为包含整数1和2；

2、如果整数的左侧出现“-”，则奇数个数认为是负整数，偶数个数认为是正整数。例如AB-1CD--2EF---3“”,认为包含整数-1、2和-3。

输出描述：

输出即为字符串中所有整数数字之和。
"""
def compute(s):
    nlen = len(s)
    total = 0
    pos = 1
    nums = 0
    for i in range(nlen):
        if s[i].isdigit():
            nums += nums * 10 + int(s[i]) * pos
        
        else:
            total += nums
            nums = 0
            if s[i] == "-":
                if i - 1 > -1 and s[i-1] == "-":
                    pos = -pos
                else:
                    pos = -1
            else:
                pos = 1
        
    total += nums
    return total
