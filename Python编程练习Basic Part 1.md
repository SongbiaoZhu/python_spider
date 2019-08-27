# Python编程练习Basic Part 1

[TOC]

## 查看当前工作目录

```python
import os
#查看当前工作目录
os.getcwd()
#修改当前工作目录
os.chdir('D:\\PythonScripts')
```

## print()换行与制表符

```python
# 可以通过打印多行字符串
print('''
Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are
	''')
# 可以通过在字符串中嵌入\n, \t
# same output with below
print('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are')
```

## write()写入文件

`f.write(string)` 会把 *string* 的内容写入到文件中，并返回写入的字符数。\n, \t等算作一个字符。写入的txt中字符串的展示方法和上述print出来的格式是一样的。

```python
>>> help(open)
>>> with open('littleStar.txt','w', encoding = 'UTF-8') as f:
	f.write('Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are.')
176
```

## read()读取文件

* `f.read(size)`，当 size 被省略或者为负的时候，将读取并返回文件的整个内容
* 注意读取时，文件对象的位置在改变，近似于一个指针的位置。如果已到达文件末尾，f.read() 将返回一个空字符串 (`''`)。

```python

>>> f = open('littleStar.txt','r', encoding = 'UTF-8')
>>> f.read()
'Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are.\n'
>>> f.read()
''
# size 是一个可选的数字参数，也可以输入读取的size
>>> f = open('littleStar.txt','r', encoding = 'UTF-8')
>>> f.read(17)
'Twinkle, twinkle,'
>>> f.read(3)
' li'
```

`f.readline()` 从文件中读取一行；换行符（`\n`）留在返回的字符串的末尾。如果 `f.readline()` 返回一个空的字符串，则表示已经到达了文件末尾，而空行使用 `'\n'` 表示，该字符串只包含一个换行符。:

```python
>>> f = open('littleStar.txt','r', encoding = 'UTF-8')
>>> f.readline()
'Twinkle, twinkle, little star,\n'
>>> f.readline()
'\tHow I wonder what you are!\n'
>>> f.readline()
'\t\tUp above the world so high,\n'
>>> f.readline()
'\t\tLike a diamond in the sky.\n'
>>> f.readline()
'Twinkle, twinkle, little star,\n'
>>> f.readline()
'\tHow I wonder what you are.\n'
>>> f.readline()
''
```

要从文件中读取行，你可以循环遍历文件对象。

```python
>>> f = open('littleStar.txt','r', encoding = 'UTF-8')
>>> for line in f:
	print(line, end = '')

	
Twinkle, twinkle, little star,
	How I wonder what you are!
		Up above the world so high,
		Like a diamond in the sky.
Twinkle, twinkle, little star,
	How I wonder what you are.
```

如果你想以列表的形式读取文件中的所有行，你也可以使用 `list(f)` 或 `f.readlines()`。

```python
>>> f = open('littleStar.txt','r', encoding = 'UTF-8')
>>> x = f.readlines()
>>> x
['Twinkle, twinkle, little star,\n', '\tHow I wonder what you are!\n', '\t\tUp above the world so high,\n', '\t\tLike a diamond in the sky.\n', 'Twinkle, twinkle, little star,\n', '\tHow I wonder what you are.\n']

>>> f = open('littleStar.txt','r', encoding = 'UTF-8')
>>> y = list(f)
>>> y
['Twinkle, twinkle, little star,\n', '\tHow I wonder what you are!\n', '\t\tUp above the world so high,\n', '\t\tLike a diamond in the sky.\n', 'Twinkle, twinkle, little star,\n', '\tHow I wonder what you are.\n']
```

## 显示当前日期和时间

```python
>>> import datetime
>>> now = datetime.datetime.now()
>>> print (now.strftime("%Y-%m-%d %H:%M:%S"))
2019-08-20 17:47:43
```

## 数学输入平方和立方计算圆面积体积

```python
# accepts the radius of a circle from the user and compute the area
>>> from math import pi
>>> r = float(input ("Input the radius of the circle : "))
Input the radius of the circle : 1
>>> print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))
The area of the circle with radius 1.0 is: 3.141592653589793
>>> print('The volume of the sphere with radius ' + str(r) + 'is' + str(pi*r**3*4/3))
The volume of the sphere with radius 1.0is4.1887902047863905
```

## 将输入的一串数转为列表或元组

```python
# accepts a sequence of comma-separated numbers from user and generate a list and a tuple
>>> values = input("Input some comma seprated numbers : ")
Input some comma seprated numbers : 2,3,5,6,7
>>> values
'2,3,5,6,7'
>>> type(values)
<class 'str'>
>>> numList = values.split(',')
>>> print(numList)
['2', '3', '5', '6', '7']
>>> numTuple = tuple(numList)
>>> print(numTuple)
('2', '3', '5', '6', '7')
```

## str.split(sep=None, maxsplit=-1) function

The function returns a list of the words of a given string using a separator as the delimiter string.

```python
# accept a filename from the user and print the extension of that.
>>> fname = input("Input the Filename: ")
Input the Filename: test.doc.txt
>>> f_ext = fname.split('.')[-1]
>>> print ("The extension of the file is : " + repr(f_ext))
The extension of the file is : 'txt'
>>> print ("The extension of the file is : " + f_ext)
The extension of the file is : txt
# repr() 函数将对象转化为供解释器读取的形式，repr(object)返回一个对象的 string 格式。类似于就是在前后各加一个单引号。
    
# The sep argument may consist of multiple characters.
>>> firstname = fname.split('.doc')[0]
>>> print(repr(firstname))
'test'
>>> print(firstname)
test
```

## 将元组中的数据依次传给字符串打印

```print
# 其实这部分仍是string.format()中的知识点
>>> a = (1,2,3,4,5,6)
>>> print('the order is: %i < %i < %i < %i < %i < %i'%a)
the order is: 1 < 2 < 3 < 4 < 5 < 6
>>> a = ('发','愤','图','强')
>>> print('%s (想)  %s (出)  %s (去)  %s (浪)！'%a)
发 (想)  愤 (出)  图 (去)  强 (浪)！

>>> date = (11,12,2014)
>>> print( "The date is  : %i / %i / %i"%date)
The date is  : 11 / 12 / 2014
```

## 打印python某一个内置函数的句法描述

A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition. Such a docstring becomes ther`__doc__` special attribute of that object.

```python
>>> print(abs.__doc__)
Return the absolute value of the argument.
>>> print(len.__doc__)
Return the number of items in a container.
```

## 打印指定某个月的日历

Use 'calendar' module.

**calendar.month(theyear, themonth, w=0, l=0):** 

The function returns a month’s calendar in a multi-line string using the formatmonth() of the TextCalendar class.

'l' specifies the number of lines that each week will use. 

```python
>>> import calendar
>>> y = int(input("Input the year : "))
Input the year : 2019
>>> m = int(input("Input the month : "))
Input the month : 8
>>> print(calendar.month(y, m))
    August 2019
Mo Tu We Th Fr Sa Su
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28 29 30 31

# l = 0或1输出是一样的，l若为2，则每一周占两行打印空间
>>> print(calendar.month(y, m, l = 2))
    August 2019

Mo Tu We Th Fr Sa Su

          1  2  3  4

 5  6  7  8  9 10 11

12 13 14 15 16 17 18

19 20 21 22 23 24 25

26 27 28 29 30 31
```

## 计算两个日期间隔的天数

```python
>>> from datetime import date
>>> f_date = date(2014, 7, 2)
>>> l_date = date(2014, 7, 11)
>>> delta = l_date - f_date
>>> print(delta.days)
9
```

## 判断是否连续相等a==b==c

```python
>>> def allEqual(x,y,z):
	return x==y==z

>>> allEqual(1,2,1)
False
>>> allEqual(1,1,1)
True
```
## 判断数字是否在1000或2000上下

```python
def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
print(near_thousand(1000))
print(near_thousand(900))
print(near_thousand(800))   
print(near_thousand(2200))
```

## 判断一个字母是否是元音字母

```python
>>> def isVowel(char):
	allVowels = 'aeiou'
	return char in allVowels

>>> print(isVowel('c'))
False
>>> print(isVowel('o'))
True
```
## 将list各元素连接转化成字符串

```python
>>> def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str(element)
    return result

>>> print(concatenate_list_data([1, 5, 12, 2]))
15122
>>> print(concatenate_list_data(['a', 'b', 'c', 'd']))
abcd
>>> ''+'a' + 'b'
'ab'
```
## 找出两个集合set中不同的元素

```python
>>> list_1 = set(["White", "Black", "Red"])
>>> list_2 = set(["Red", "Green"])
>>> list_1.difference(list_2)
{'Black', 'White'}
>>> list_2.difference(list_1)
{'Green'}
```
## 计算两个数字的最大公约数

greatest common divisor (GCD) of two positive integers

```python
>>> def gcd(x, y):
    gcd = 1
    
    if x % y == 0:
        return y
    
    for k in range(int(y / 2), 0, -1):
        if x % k == 0 and y % k == 0:
            gcd = k
            break  
    return gcd

>>> print(gcd(12, 17))
1
>>> print(gcd(4, 6))
2
>>> print(gcd(12, 16))
4
```
## 计算两个数的最小公倍数

least common multiple (LCM) of two positive integers.

```python
>>> def lcm(x, y):
   if x > y:
       z = x
   else:
       z = y

   while(True):
       if((z % x == 0) and (z % y == 0)):
           lcm = z
           break
       z += 1

   return lcm

>>> print(lcm(4, 6))
12
>>> print(lcm(15, 17))
255
```
## 判断3个数中是否至少有两个数相等

Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

```python
>>> def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

>>> print(sum(2, 1, 2))
0
>>> print(sum(1, 2, 3))
6
```
## 判断一个是否在某一数值范围内

Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

```python
>>> def sum(x, y):
    sum = x + y
    if sum in range(15, 20):
        return 20
    else:
        return sum

>>> print(sum(10, 6))
20
>>> print(sum(10, 2))
12
```
## 判断三个条件是否至少一个为真

Write a Python program which will return true if the two given integer values are equal or their sum or difference is 5.

```python
>>> def test_number5(x, y):
    if x == y or abs(x-y) == 5 or (x+y) == 5:
        return True
    else:
        return False

>>> print(test_number5(7, 2))
True
>>> print(test_number5(3, 2))
True
>>> print(test_number5(2, 2))
True
```
## 判断数据类型为整形integer

Write a Python program to add two objects if both objects are an integer type.

isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。 

`isinstance(object, classinfo)`

* object -- 实例对象。classinfo -- 可以是直接或间接类名、基本类型或者由它们组成的元组。

```python
>>> def add_numbers(a, b):
    if not (isinstance(a, int) and isinstance(b, int)):
         raise TypeError("Inputs must be integers")
    return a + b

>>> print(add_numbers(10, 20))
30
>>> print(add_numbers(10, 20.0))
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    print(add_numbers(10, 20.0))
  File "<pyshell#255>", line 3, in add_numbers
    raise TypeError("Inputs must be integers")
TypeError: Inputs must be integers

# classinfo是类型组成的元组
>>>a = 2
>>> isinstance (a,(str,int,list))    # 是元组中的一个返回 True
True
```

## 计算本金利率利润

* 几次方的用法
* **round()** 方法返回浮点数x的四舍五入值。
* `round( x [, n]  )` 
* x -- 数值表达式。
* n -- 数值表达式，保留几位小数。

```python
>>> amt = 10000
>>> int = 3.5
>>> years = 7
>>> future_value  = amt*((1+(0.01*int)) ** years)
>>> print(round(future_value,2))
12722.79

# round()实例
round(70.23456) :  70
round(56.659,1) :  56.7
round(80.264, 2) :  80.26
round(100.000056, 3) :  100.0
round(-100.000056, 3) :  -100.0
```
## 判断python shell是32bit还是64bit

```python
>>> import struct
>>> print(struct.calcsize("P") * 8)
64
```
## 判断运行电脑的平台名称和系统版本

```python
>>> import platform
>>> import os
>>> print(os.name)
nt
>>> print(platform.system())
Windows
>>> print(platform.release())
7
```
## 将字符串解析为浮点型或整形

`int()` 需要对浮点型进行操作。

```python
>>> n = "246.2458"
>>> print(float(n))
246.2458
>>> print(int(float(n)))
246
>>> print(int(n))
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    print(int(n))
ValueError: invalid literal for int() with base 10: '246.2458'
```
## 打印不换行

 Write a Python program to print without newline or space?

```python
>> for i in range(0, 10):
    print('*', end="")

    
**********
```
## 获取当前的系统用户名

```python
>>> import getpass
>>> print(getpass.getuser())
samsung
```

## 计时一个函数的运行时间

 Write a program to get execution time for a Python method.

```python
>>> import time
>>> def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

>>> n = 5
>>> print("\nTime to sum of 1 to ",n," and required time to calculate is :",sum_of_n_numbers(n))

Time to sum of 1 to  5  and required time to calculate is : (15, 0.0)
```

## Python os.path() 模块

[os.path module](https://www.runoob.com/python/python-os-path.html)

os.path 模块主要用于获取文件的属性。

```python

```
## 64



```python

```
## python



```python

```
## python



```python

```
## python



```python

```
## python



```python

```
## python



```python

```
## python



```python

```
## python



```python

```

