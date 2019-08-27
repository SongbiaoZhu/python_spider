# Python中的split()函数的用法

## 摘要

Python中有split()和os.path.split()两个函数，具体作用如下：

* split()：拆分字符串。通过指定分隔符对字符串进行切片，并返回分割后的字符串列表（list）
* os.path.split()：按照路径将文件名和路径分割开

## 函数使用说明

1、split()函数
语法：str.split(str="",num=string.count(str))[n]

参数说明：
str:表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
num:表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量

[n]: 表示选取第n个分片

注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略

 

2、os.path.split()函数
语法：os.path.split('PATH')

参数说明：

1.PATH指一个文件的全路径作为参数：

2.如果给出的是一个目录和文件名，则输出路径和文件名

3.如果给出的是一个目录名，则输出路径和为空文件名

## 实例代码

```python
# 1.以'.'为分隔符
string = "www.gziscas.com.cn"
print(string.split('.'))
# ['www', 'gziscas', 'com', 'cn']

# 2.分割两次
print(string.split('.'，2))
# ['www', 'gziscas', 'com.cn']

# 3.分割两次，并取序列为1的项
print(string.split('.',2)[1])
# gziscas

# 4.分割两次，并把分割后的三个部分保存到三个文件
u1, u2, u3 =string.split('.',2)
print(u1)—— www
print(u2)—— gziscas
print(u3) ——com.cn

# 5. 多次分割串联
str="hello boy<[www.baidu.com]>byebye"
print(str.split("[")[1].split("]")[0])
# www.baidu.com

# 三、分离文件名和路径
import os
print(os.path.split('/dodo/soft/python/'))
# ('/dodo/soft/python', '')

print(os.path.split('/dodo/soft/python'))
# ('/dodo/soft', 'python')


```

