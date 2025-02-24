# Python笔记

> [!IMPORTANT]
>
> 成都顺盛科技有限公司 课程

## 项目规范

在Python文件最上方写入如下注释（多行注释）：

```python
'''
    项目名称：名称
    项目描述：项目的描述
    项目环境：Python 3.11.10
    作者所属：小猫头鹰
    创建时间：2024年11月21日
'''
```

## 关键字（特殊含义）

### 查看关键字

```python
import keyword
print(keyword.kwlist)
```

### 关键字：

```
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

1. $$
   1. False：布尔类型的值，表示假，与True想反
   2. None ：None比较特殊，表示什么也没有，他有自己的数据类型 -NoneType
   3. True：布尔类型的值，表示真，与False相反
   4. and：用于表达式运算，逻辑与操作
   5. as：用于类型转换，取别名
   6. assert：断言，用于判断变量或者条件表达式的值是否为真
   7. async：声明一个函数为异步函数
   8. await：声明程序挂起
   9. break：中断循环语句的执行
   10. class：用于定义类
   11. continue：跳出本次循环，继续执行下一次循环
   12. def：用于定义函数或方法
   13. del：删除变量或序列的值
   14. elif：条件语句，与if、else结合使用
   15. else：条件语句，与if、else结合使用，也可用于异常和循环语句
   16. except：except包含捕获异常后的操作代码块，与try、finally结合使用
   17. finally：用于异常语句，出现异常后，始终要执行finally包含的代码块，与try、except结合使用
   18. for：for循环语句
   19. from：用于导入模块，与import结合使用
   20. global：定义全局变量
   21. if：条件语句，与else、elif结合使用
   22. import：用于导入模块，与form结合使用
   23. in：判断变量是否在序列中
   24. is：判断变量是否为某个类的实例
   25. lambda：定义匿名函数
   26. nonlocal：用于标识外部作用域的变量
   27. not：用于表达式运算，逻辑或非操作
   28. or：用于表达式运算，逻辑或操作
   29. pass：空的类，方法或函数的占位符
   30. raise：异常抛出操作
   31. return：用于从函数返回计算结果
   32. try：try包含可能会出现异常的语句，与except、finally结合使用
   33. while：while循环语句
   34. with：简化python语句
   35. yield：用于从函数依次返回值
   $$

## 下标

以 **python**为例

| 位置 | p    | y    | t    | h    | o    | n    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 正向 | 0    | 1    | 2    | 3    | 4    | 5    |
| 逆向 | -6   | -5   | -4   | -3   | -2   | -1   |

取全部反向数据：`print(a[::-1])`。

数据取反 -- 重点在**-1**（方向符），而不是区间。

```python
print(a[8:2:-1])
# 如果8:2反向为2:8，则逻辑错误，输出含有问题。
```

### 列表

列表嵌套的数据取出

```python
# 取出 Catherine Erin。
a = ["小猫头鹰","youngowl",["猫头鹰","Catherine Erin"],"原神"]
print(a[2][1])
```

### 元组

```
组内只有一条数据-->，需要在数据后面加上“,”。
否则则被认为是 字符串。
```

## 格式化输出

格式

```python
time = 2.5
name = "小猫头鹰"
age = 19
ltd = "米哈游"
hobby = "动漫、cosplay"

# 其中f可以大写。
print(f"大家好，我是练习时长两年半的个人练习生，{name}，{age}岁，来自{ltd}，我喜欢{hobby}。")
# 占位符
print("大家好，我是练习时长%.2f的个人练习生，%s，%d岁，来自%s，我喜欢%s。"%(time,name,age,ltd,hobby))
# format
print("大家好，我是练习时长{0}的个人练习生，{1}，{2}岁，来自{3}，我喜欢{4}。\n我的好朋友也喜欢{4}。".format(time,name,age,ltd,hobby))
```

`%f`（默认保留**6**位小数）：`%.1f`（1位）、`%.5f`（5位）可以实现保留小数点相应位数。

## 字符编码

主要用于**开发网站**处理**后台数据**。
打开文件之前需要先知道文件的编码。

```python
# 通过字符找编码序号
print(ord("猫"))
# 通过编码序号找字符
print(chr(12345))
```

## 条件循环

### 判断语句

1为真，0为假。

```python
import math
if 1:
    print(math.factorial(5))
else:
    print(math.sqrt(6))
```

上述代码输出为120，将1改成0，则输出2.449489742783178。

程序从上往下执行，注意**<u>上一条件</u>是否已经包含了<u>下一条件</u>**。

### 循环语句

while

先判断后输出更好。
