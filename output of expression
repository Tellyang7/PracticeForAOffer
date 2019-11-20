"""
题目描述：
常用的逻辑计算有And（表示为&）；Or（表示为|）；Not（表示为！）。其中，他们的优先级关系是Not（！）>And（&）>Or（|）。


输入描述：
1、测试用例中间无空格，无需考虑空格。

2、测试用例表达式只会出现如下字符：“0”，“1”，“（”，“）”，“&”，“|”，“！”。

3、测试用例所给的输入都是合法输入，无需要考虑非法输入。

4、测试用例长度不会超过128个字符。

5、括号可以重复嵌套。

例如：

1 | ( 1 & 0 )                       返回值：1

1 & 0 | 0 & 1                     返回值：0

! 0 & 1 | 0                          返回值：1

( ( ! 0 & 1 ) ) | 0                 返回值：1


输出描述：
输出逻辑运算后的最终结果：0或者1

示例1：
输入：! ( 1 & 0 ) | 0 & 1

输出：1

示例2：
输入：! ( 1 & 0 ) & 0 | 0

"""

def check(s):
    exp1 = list()
    i = 0
    while i < len(s):
        if s[i] == "!":
            if s[i+1] == "0":
                exp1.append("1")
            else:
                exp1.append("0")
            i += 2
            continue
        exp1.append(s[i])
        i += 1
    s = "".join(exp1)
    
    j = 0
    exp2 = list()
    while j < len(s):
        if s[j] == "&":
            exp2.pop()
            if s[j-1] == s[j+1] and s[j-1] == "1":
                exp2.append("1")
            else:
                exp2.append("0")
            j += 2
            continue
        exp2.append(s[j])
        j += 1
    s = "".join(exp2)

    k = 0
    exp3 = list()
    while k < len(s):
        if s[k] == "|":
            exp3.pop()
            if s[k+1] == s[k-1] and s[k+1] == "0":
                exp3.append("0")
            else:
                exp3.append("1")
            k += 2
            continue
        exp3.append(s[k])
        k += 1
    s = "".join(exp3)
    return s
    
   
   def push_all(s):
    s = s.replace(" ","")
    print(s)
    exp = list()
    for i in range(len(s)):
        if(s[i] == ")"):
            m = len(exp) - 1
            texp = list()
            while(exp[m] != "("):
                tt = exp.pop()
                print(tt)
                texp.append(tt)
                m -= 1
            
            exp.pop()
            texp.reverse()
            val = check("".join(texp))
            exp.append(val)
            continue
        exp.append(s[i])
    return check("".join(exp)) 
    
    # test..
    push_all("( ( ! 0 & 1 ) ) | 0")
