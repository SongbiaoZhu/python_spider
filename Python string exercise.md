# string exercise Python

[TOC]

## 统计一个字符串中的每个字符的频率

Write a Python program to count the number of characters (character frequency) in a string.

```python
>>> def charFreq(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

>>> print(charFreq('google.com'))
{'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}
```
## 统计一个字符串中每个单词的频率

Write a Python program to count the occurrences of each word in a given sentence.

* 将一句话式的字符串(如由空格分隔的一串单词)转化为列表`words = str.split()`

* 字典的keys的遍历，并且遍历key时change value

```python
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

>>> print( word_count('the quick brown fox jumps over the lazy dog.'))
{'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog.': 1}

# zhs
>>> def wordFreq(str):
	freq = {}
	words = str[:len(str)-1].split()
	for e in words:
		keys = freq.keys()
		if e in keys:
			freq[e] +=1
		else:
			freq[e] = 1
	return freq

>>> print( wordFreq('the quick brown fox jumps over the lazy dog.'))
{'the': 2, 'quick': 1, 'brown': 1, 'fox': 1, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
```

## 将字符串中两个特定字符之间的内容替换为其他字符

`str1.find('not')`

`str1.replace(str1[snot:(spoor+4)], 'good')`

```python
>>> def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1

>>> print(not_poor('The lyrics is not that poor!'))
The lyrics is good!
>>> print(not_poor('The lyrics is poor!'))
The lyrics is poor!
```
## 找到字符串中最长的单词

Write a Python function that takes a list of words and returns the length of the longest one.

```python
>>> def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

>>> print(find_longest_word(["PHP", "Exercises", "Backend"]))
Exercises

# 自己通过max函数写了另一个函数
>>> def longestWord(wordList):
	lstword = ''
	length = []
	for n in wordList:
		length.append(len(n))
		if len(n) == max(length):
			lstword = n
	return lstword

>>> print(longestWord(["PHP", "Exercises", "Backend"]))
Exercises
>>> print(longestWord(["PHPPHPPHPPHPPHP", "Exercises", "Backend"]))
PHPPHPPHPPHPPHP
# 第一个代码的优势在于，.sort函数，还可以返回其他第2长，第3，第4的单词
```
## 移去字符串中的第n个字符

Write a Python program to remove the nth index character from a nonempty string.

```python
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part

>>> print(remove_char('Python', 0))
ython

# zhs write
>>> def removeChar(str, n):
	newstr = str.replace(str[n-1],'')
	return newstr

>>> print(removeChar('Python', 3))
Pyhon
```
## 交换字符串的首尾字符

Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

```python
>>> def change_sring(str1):
      return str1[-1:] + str1[1:-1] + str1[:1]

>>> print(change_sring('abcd'))
dbca
>>> print(change_sring('12345'))
52341
```
## 移除字符串中奇数位置的字符 

Write a Python program to remove the characters which have odd index values of a given string.

```python
>>> def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

>>> print(odd_values_string('abcdef'))
ace

# zhs
>>> def rmOdd(str):
	newstr = ''
	for i in range(0,len(str),2):
		newstr += str[i]
	return newstr

>>> rmOdd('abcdef')
'ace'
```
## 将输入的字符串进行大小写转换 

Write a Python script that takes input from the user and displays that input back in upper and lower cases.

`.upper()`

`.lower()`

```python
>>> user_input = input("What's your favourite language? ")
What's your favourite language? english
>>> print("My favourite language is ", user_input.upper())
My favourite language is  ENGLISH
>>> print("My favourite language is ", user_input.lower())
My favourite language is  english
```
## 挑选出字符串中不重复的单词并按字母顺序排列

Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

* `input()` 默认返回字符串
* `[i for i in str.split(',')]` 将字符串转换为列表 （某一分隔符）
* `set(list)` 取列表中的unique元素
* `sorted(list)` 排序列表
* `','join(list)` 可以将列表转化成字符串 （某一分隔符）

```python
>>> items = input("Input comma separated sequence of words:")
Input comma separated sequence of words:red,green,red,black,pink,pink,yellow
>>> words = [word for word in items.split(",")]
>>> print(",".join(sorted(list(set(words)))))
black,green,pink,red,yellow
```
## 将一个字符串转化为html标签格式

Write a Python function to create the HTML string with tags around the word(s).

```python
>>> def add_tags(tag, word):
	return "<%s>%s</%s>" % (tag, word, tag)

>>> print(add_tags('i', 'Python'))
<i>Python</i>

# zhs
>>> def add_tags(tag, word):
	return "<{}>{}</{}>".format(tag, word, tag)

>>> print(add_tags('i', 'Python'))
<i>Python</i>
```
## 从字符串最后面进行分割字符串 

Write a Python program to get the last part of a string before a specified character.

Python rsplit() 方法通过指定分隔符对字符串进行分割并返回一个列表，默认分隔符为所有空字符，包括空格、换行(\n)、制表符(\t)等。类似于 [split()](http://www.cnblogs.com/wushuaishuai/p/7687294.html) 方法，只不过是从字符串最后面开始分割。

* `S.rsplit([sep``=``None``][,count``=``S.count(sep)])` 返回分割后的字符串列表。
* sep -- 可选参数，指定的分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
* count -- 可选参数，分割次数，默认为分隔符在字符串中出现的总次数。
* [rsplit example](https://www.cnblogs.com/wushuaishuai/p/7792874.html)

```python
>>> str1 = 'https://www.w3resource.com/python-exercises/string'
>>> print(str1.rsplit('/', 1)[0])
https://www.w3resource.com/python-exercises
>>> print(str1.rsplit('-', 1)[0])
https://www.w3resource.com/python
```
## 将字符串逆序并得到一个逆序后的字符串

Write a Python function to reverse a string if it's length is a multiple of 4.

[reversed](https://www.runoob.com/python3/python3-func-reversed.html)

```python
>>> def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

>>> print(reverse_string('python'))
python
#注意reversed(str)返回一个反转的迭代器，需要进行join来转成string
>>> str = 'abcd'
>>> reversed(str)
<reversed object at 0x0000000003230E08>
>>> print(reversed(str))
<reversed object at 0x0000000003230FC8>
>>> print(''.join(reversed(str)))
dcba
```
## 判断字符串中的字母是否为大写

Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

```python
>>> def to_uppercase(str1):
    num_upper = 0
    for letter in str1[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str1.upper()
    return str1

>>> print(to_uppercase('Python'))
Python
>>> print(to_uppercase('PyThon'))
PYTHON
```
## 删除 string 末尾的指定字符（默认为空格）

`str.rstrip([chars])` 

* chars -- 指定删除的字符（默认为空格）

```python
>>> str = "     this is string example....wow!!!\n    \t"
>>> print(str) #会打印出换行以及空格以及制表符
     this is string example....wow!!!
    	
>>> print(str.rstrip())
     this is string example....wow!!!
>>> str = "88888888this is string example....wow!!!8888888"
>>> print(str.rstrip('8'))
88888888this is string example....wow!!!
```
## startswith()方法

Python startswith() 方法用于检查字符串是否是以指定子字符串开头，如果是则返回 True，否则返回 False。如果参数 beg 和 end 指定值，则在指定范围内检查。

`str.startswith(str, beg=0,end=len(string))` ; 如果检测到字符串则返回True，否则返回False。

- str -- 检测的字符串。
- strbeg -- 可选参数用于设置字符串检测的起始位置。
- strend -- 可选参数用于设置字符串检测的结束位置。

```python
>>> str = "this is string example....wow!!!";
>>> print(str.startswith( 'this' ))
True
>>> print(str.startswith( 'is', 2, 4 ))
True
>>> print(str.startswith( 'this', 2, 4 ))
False
```
## 凯撒密码 Caesar shift

##  Write a Python program to create a Caesar encryption.

```python
#https://gist.github.com/nchitalov/2f2b03e5cf1e19da1525
>>> def caesar_encrypt(realText, step):
	outText = []
	cryptText = []
	
	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in realText:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = uppercase[crypting]
			outText.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + step) % 26
			cryptText.append(crypting)
			newLetter = lowercase[crypting]
			outText.append(newLetter)
	return outText

>>> code = caesar_encrypt('abc', 2)
>>> print(code)
['c', 'd', 'e']
>>> print(''.join(code))
cde
>>> print(repr(''.join(code)))
'cde' 
```
## 排序函数sort()与sorted()

Python list内置sort()方法用来排序，也可以用python内置的全局sorted()方法来对可迭代的序列排序生成新的序列.

* 使用sort()方法对list排序会修改list本身,不会返回新list，通常此方法不如sorted()方便
* sort()不能对dict字典进行排序
* sorted()可以对字典排序，默认会按照dict的key值排序，返回的结果是一个对key值排序好的list
* list.sort()和sorted()函数，有一个key参数，key参数来指定一个函数，此函数将在每个元素比较前被调用。**key参数的值为一个函数，此函数只有一个参数且返回一个值用来进行比较**。

```python
# sort()用法
>>> my_list = [3, 5, 1, 4, 2]
>>> my_list.sort()
>>> print(my_list)
[1, 2, 3, 4, 5]
# sorted()用法
>>> my_list = [3, 5, 1, 4, 2]
>>> result = sorted(my_list)
>>> print(result)
[1, 2, 3, 4, 5]
# sorted()可以排序字典，返回key 排序后的 key list.
>>> my_dict = {"a":"1", "c":"3", "b":"2"}
>>> result = sorted(my_dict)
>>> print(result)
['a', 'b', 'c']
# 通过设置key参数，可以对字典根据value进行排序
>>> my_dict = {"a":"2", "c":"5", "b":"1"}
>>> result2 = sorted(my_dict, key=lambda x:my_dict[x])
>>> print(result2)
['b', 'a', 'c']
# 通过设置key参数，可以复杂的嵌套列表排序
>>> student_tuples = [('john', 'A', 15),('jane', 'B', 12),('dave', 'B', 10),]
>>> result = sorted(student_tuples, key=lambda student: student[2])
>>> print(result)
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
```
## 浮点型保留两位小数并且四舍五入 

`.format(x)` 函数

```python
# 四舍五入保留两位小数
>>> x = 3.1415926
>>> y = 12.9999
>>> print("Formatted Number: "+"{:.2f}".format(x));
Formatted Number: 3.14
>>> print("Original Number: ", x)
Original Number:  3.1415926
>>> print("Original Number: ", y)
Original Number:  12.9999
>>> print("Formatted Number: "+"{:.2f}".format(y));
Formatted Number: 13.00

# 四舍五入保留两位小数并且添加正负号
>>> print("Formatted Number with sign: "+"{:+.2f}".format(x))
Formatted Number with sign: +3.14
>>> y = -12.9999
>>> print("Formatted Number with sign: "+"{:+.2f}".format(y))
Formatted Number with sign: -13.00
    
# 四舍五入去除小数部分
>>> print("Formatted Number with no decimal places: "+"{:.0f}".format(x))
Formatted Number with no decimal places: 3
>>> print("Formatted Number with no decimal places: "+"{:.0f}".format(y))
Formatted Number with no decimal places: -13
 
# 输出固定宽度的整形，在左边或者右边填充0 或者*等符号
>>> x = 3
>>> y = 123
>>> print("Formatted Number(left padding, width 2): "+"{:0>2d}".format(x))
Formatted Number(left padding, width 2): 03
>>> print("Formatted Number(left padding, width 6): "+"{:0>6d}".format(y))
Formatted Number(left padding, width 6): 000123
>>> print("Formatted Number(right padding, width 2): "+"{:*< 3d}".format(x))
Formatted Number(right padding, width 2):  3*
>>> print("Formatted Number(right padding, width 6): "+"{:*< 7d}".format(y))
Formatted Number(right padding, width 6):  123***

# 对大额数字添加分号分割显示
>>> x = 3000000
>>> print("Formatted Number with comma separator: "+"{:,}".format(x))
Formatted Number with comma separator: 3,000,000
    
# 将数字转为百分比显示
>>> x = 0.25
>>> print("Formatted Number with percentage: "+"{:.2%}".format(x))
Formatted Number with percentage: 25.00%
>>> y = -0.25
>>> print("Formatted Number with percentage: "+"{:.2%}".format(y))
Formatted Number with percentage: -25.00%
    
# 固定数字输出的宽度，分别设置数字左对齐 居中 或者右对齐
>>> x = 22
>>> print("Original Number: ", x)
Original Number:  22
>>> print("Left aligned (width 10)   :"+"{:< 10d}".format(x))
Left aligned (width 10)   : 22       
>>> print("Right aligned (width 10)  :"+"{:10d}".format(x))
Right aligned (width 10)  :        22
>>> print("Center aligned (width 10) :"+"{:^10d}".format(x))
Center aligned (width 10) :    22 
```
## 统计字符串里某个字字符串出现的次数

`str.count(sub, start= 0,end=len(string))`

- sub -- 搜索的子字符串
- start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
- end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

```python
>>> str1 = 'The quick brown fox jumps over the lazy dog.'
>>> print(str1.count("fox"))
1
```
## 将字符串倒序排列得到一个新的字符串

* reverse a string

```python
>>> def reverse_string(str1):
    return ''.join(reversed(str1))

>>> print(reverse_string("abcdef"))
fedcba
```
## 将字符串中所有单词顺序倒序排列

* reverse words in the string

`[::-1]` 顺序相反操作

```python
>>> a = [1,3,4,2,'a','d']
>>> print (a[::-1])
['d', 'a', 2, 4, 3, 1]

>>> def reverse_string_words(text):
    for line in text.split('\n'):
        return(' '.join(line.split()[::-1]))

>>> print(reverse_string_words("The quick brown fox jumps over the lazy dog."))
dog. lazy the over jumps fox brown quick The
```
## 去除字符串中零散出现的特定某几个字母

Write a Python program to strip a set of characters from a string.

```python
>>> def strip_chars(str, chars):
    return "".join(c for c in str if c not in chars)

>>> print(strip_chars("The quick brown fox jumps over the lazy dog.", "aeiou"))
Th qck brwn fx jmps vr th lzy dg.
```
## 打印平方厘米和立方厘米

以及嵌套的.format函数用法

```python
>>> area = 1256.66
>>> volume = 1254.725
>>> decimals = 2
>>> print("The area of the rectangle is {0:.{1}f}cm\u00b2".format(area, decimals))
The area of the rectangle is 1256.66cm²
>>> print("The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals))
The volume of the cylinder is 1254.72cm³
```
## 打印字符串中每一个字符的位置index

Write a Python program to print the index of the character in a string.

* enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中。
* `enumerate(sequence, [start=0])` ;
* sequence -- 一个序列、迭代器或其他支持迭代对象。start -- 下标起始位置。

```python
>>> str1 = "w3resource"
>>> for index, char in enumerate(str1):
    print("Current character", char, "position at", index )

    
Current character w position at 0
Current character 3 position at 1
Current character r position at 2
Current character e position at 3
Current character s position at 4
Current character o position at 5
Current character u position at 6
Current character r position at 7
Current character c position at 8
Current character e position at 9
```
## 判断一个字符串是否包含所有26个字母

Write a Python program to check if a string contains all letters of the alphabet.

```python
>>> import string
>>> alphabet = set(string.ascii_lowercase)
>>> input_string = 'The quick brown fox jumps over the lazy dog'
>>> print(set(input_string.lower()) >= alphabet)
True
>>> input_string = 'The quick brown fox jumps over the lazy cat'
>>> print(set(input_string.lower()) >= alphabet)
False
```
## 将固定分隔的字符串转化成列表

Write a Python program to convert a string in a list.

```python
>>> str1 = "The quick brown fox jumps over the lazy dog."
>>> print(str1.split(' '))
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
>>> str1 = "The-quick-brown-fox-jumps-over-the-lazy-dog."
>>> print(str1.split('-'))
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']
```
## 统计字符串中所有的元音字母并显示

Write a Python program to count and display the vowels of a given text.

```python
>>> def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])

    
>>> vowel('w3resource')
4
['e', 'o', 'u', 'e']
```
## 找到字符串中第一个非重复的字符

Write a Python program to find the first non-repeating character in given string.

```python
>>> def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None

>>> print(first_non_repeating_character('abcdef'))
a
>>> print(first_non_repeating_character('abcabcdef'))
d
```
## 在给定字符串中随机抽样一个字符若干次并排列

Write a Python program to print all permutations with given repetition number of characters of a given string.

```python
>>> from itertools import product
>>> def all_repeat(str1, rno):
  chars = list(str1)
  results = []
  for c in product(chars, repeat = rno):
    results.append(c)
  return results

>>> print(all_repeat('xy', 3))
[('x', 'x', 'x'), ('x', 'x', 'y'), ('x', 'y', 'x'), ('x', 'y', 'y'), ('y', 'x', 'x'), ('y', 'x', 'y'), ('y', 'y', 'x'), ('y', 'y', 'y')]
>>> print(all_repeat('xyz', 2))
[('x', 'x'), ('x', 'y'), ('x', 'z'), ('y', 'x'), ('y', 'y'), ('y', 'z'), ('z', 'x'), ('z', 'y'), ('z', 'z')]
```
## 找到字符串中第一个发生重复的字符

Write a Python program to find the first repeated character in a given string.

```python
>>> def first_repeated_char(str1):
  for index,c in enumerate(str1):
    if str1[:index+1].count(c) > 1:
      return c 
  return "None"

>>> print(first_repeated_char("abcdabcd"))
a
>>> print(first_repeated_char("abcd"))
None
```
## 返回字符串中出现频率第二高的单词

Write a Python program to find the second most repeated word in a given string.

```python
>>> def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    counts_x = sorted(counts.items(), key=lambda kv: kv[1])
    #print(counts_x)
    return counts_x[-2]

>>> print(word_count("Both of these issues are fixed by postponing the evaluation of annotations. Instead of compiling code which executes expressions in annotations at their definition time, the compiler stores the annotation in a string form equivalent to the AST of the expression in question. If needed, annotations can be resolved at runtime using typing.get_type_hints(). In the common case where this is not required, the annotations are cheaper to store (since short strings are interned by the interpreter) and make startup time faster."))
('of', 4)
```
## 找到字符串中出现频率最高的字母

Write a Python program to find the maximum occurring character in a given string.

```python
>>> def get_max_occuring_char(str1):
  ASCII_SIZE = 256
  ctr = [0] * ASCII_SIZE
  max = -1
  ch = ''
  for i in str1:
    ctr[ord(i)]+=1;
 
  for i in str1:
    if max < ctr[ord(i)]:
      max = ctr[ord(i)]
      ch = i
  return ch

>>> print(get_max_occuring_char("abcdefghijkb"))
b
```

## 把字符串中所有的空格都挪到字符串开始

```python
>>> def move_Spaces_front(str1):
  noSpaces_char = [ch for ch in str1 if ch!=' ']
  spaces_char = len(str1) - len(noSpaces_char)
  result = ' '*spaces_char
  result = '"'+result + ''.join(noSpaces_char)+'"' #为了打印时开始结尾有双引号
  return(result)

>>> print(move_Spaces_front("w3resource .  com  "))
"     w3resource.com"
>>> print(move_Spaces_front("   w3resource.com  "))
"     w3resource.com"
```
## 将字符串中每个单词的首字母和尾字母转大写

Write a Python program to capitalize first and last letters of each word of a given string.

` str1.title()` 将每个单词的首字母大写。

```python
>>> def capitalize_first_last_letters(str1):
     str1 = result = str1.title()
     result =  ""
     for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]

>>> print(capitalize_first_last_letters("python exercises practice solution"))
PythoN ExerciseS PracticE SolutioN
```
## 计算一个字符串中出现的所有数字的和

```python
>>> def sum_digits_string(str1):
    sum_digit = 0
    for x in str1:
        if x.isdigit() == True:
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit

>>> print(sum_digits_string("123abcd45"))
15
```
## 返回二进制字符串中0连续出现的最大次数

```python
>>> def max_consecutive_0(input_str): 
     return  max(map(len,input_str.split('1')))

>>> str1 = '111000010000110'
>>> print(max_consecutive_0(str1))
4
```
## 去除字符串中连续重复的字符

Write a Python program to remove all consecutive duplicates of a given string.

```python
>>> from itertools import groupby
>>> def remove_all_consecutive(str1): 
	result_str = [] 
	for (key,group) in groupby(str1): 
		result_str.append(key) 

	return ''.join(result_str)

>>> str1 = 'xxxxxyyyyy'
>>> print("Original string:" + str1)
Original string:xxxxxyyyyy
>>> print("After removing consecutive duplicates: " + str1)
After removing consecutive duplicates: xxxxxyyyyy
>>> print(remove_all_consecutive(str1))
xy
```
## 将字符串中不重复的字符和重复的字符分开

Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string.

```python
>>> from collections import Counter
>>> def generateStrings(input): 
     str_char_ctr = Counter(input) 
     part1 = [ key for (key,count) in str_char_ctr.items() if count==1] 
     part2 = [ key for (key,count) in str_char_ctr.items() if count>1] 
     part1.sort() 
     part2.sort()
     return part1,part2

>>> input = "aabbcceffgh"
>>> s1, s2 = generateStrings(input)
>>> print(''.join(s1))
egh
>>> print(''.join(s2))
abcf
```
## 找出两个字符串中最长的共同字符串

Write a Python program to find the longest common sub-string from two given strings.

```python
>>> from difflib import SequenceMatcher
>>> def longest_Substring(s1,s2): 
  
     seq_match = SequenceMatcher(None,s1,s2) 
  
     match = seq_match.find_longest_match(0, len(s1), 0, len(s2)) 
  
     # return the longest substring 
     if (match.size!=0): 
          return (s1[match.a: match.a + match.size])  
     else: 
          return ('Longest common sub-string not present')

        
>>> s1 = 'abcdefgh'
>>> s2 = 'xswerabcdwd'
>>> print("Original Substrings:\n",s1+"\n",s2)
Original Substrings:
 abcdefgh
 xswerabcdwd
>>> print("\nCommon longest sub_string:")

Common longest sub_string:
>>> print(longest_Substring(s1,s2))
abcd
```
## 找出两个字符串中互不相同的字符

Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings. 

```python
>>> def uncommon_chars_concat(s1, s2):   
     
     set1 = set(s1) 
     set2 = set(s2) 
  
     common_chars = list(set1 & set2) 
     result = [ch for ch in s1 if ch not in common_chars] + [ch for ch in s2 if ch not in common_chars] 
     return(''.join(result))

>>> s1 = 'abcdpqr'
>>> s2 = 'xyzabcd'
>>> print("Original Substrings:\n",s1+"\n",s2)
Original Substrings:
 abcdpqr
 xyzabcd
>>> print("\nAfter concatenating uncommon characters:")

After concatenating uncommon characters:
>>> print(uncommon_chars_concat(s1, s2))
pqrxyz
```
## 将字符串中的空格都移到字符开始

Write a Python program to move all spaces to the front of a given string in single traversal. 

```python
>>> def moveSpaces(str1): 
    no_spaces = [char for char in str1 if char!=' ']   
    space= len(str1) - len(no_spaces)
    # Create string with spaces
    result = ' '*space    
    return result + ''.join(no_spaces)

>>> s1 = "Python Exercises"
>>> print(moveSpaces(s1))
 PythonExercises
>>> print(s1)
Python Exercises
```
## 统计字符串中大写、小写、数字和特殊符号的个数

Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.

```python
>>> def count_chars(str):
     upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
          elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
          else: special_ctr += 1
     return upper_ctr, lower_ctr, number_ctr, special_ctr

>>> str = "@W3Resource.Com"
>>> u, l, n, s = count_chars(str)
>>> print('Upper case characters: ',u)
Upper case characters:  3
>>> print('Lower case characters: ',l)
Lower case characters:  9
>>> print('Number case: ',n)
Number case:  1
>>> print('Special case characters: ',s)
Special case characters:  2
```

## 找出字符串A中包含字符串B所有字符的最小窗口

Write a Python program to find the minimum window in a given string which will contain all the characters of another given string.

```python
>>> import collections
>>> def min_window(str1, str2):
    result_char, missing_char = collections.Counter(str2), len(str2)
    i = p = q = 0
    for j, c in enumerate(str1, 1):
        missing_char -= result_char[c] > 0
        result_char[c] -= 1
        if not missing_char:
            while i < q and result_char[str1[i]] < 0:
                result_char[str1[i]] += 1
                i += 1
            if not q or j - i <= q - p:
                p, q = i, j
    return str1[p:q]

>>> str1 = "PRWSOERIUSFK"
>>> str2 = "OSU"
>>> print(min_window(str1,str2))
OERIUS
```
## 找出包含字符串中所有字符的最小窗口

Write a Python program to find smallest window that contains all characters of a given string.

```python
>>> from collections import defaultdict
>>> def find_sub_string(str): 
    str_len = len(str) 
      
    # Count all distinct characters. 
    dist_count_char = len(set([x for x in str])) 
  
    ctr, start_pos, start_pos_index, min_len = 0, 0, -1, 9999999999
    curr_count = defaultdict(lambda: 0) 
    for i in range(str_len): 
        curr_count[str[i]] += 1
 
        if curr_count[str[i]] == 1: 
            ctr += 1
  
        if ctr == dist_count_char: 
            while curr_count[str[start_pos]] > 1: 
                if curr_count[str[start_pos]] > 1: 
                    curr_count[str[start_pos]] -= 1
                start_pos += 1
  
            len_window = i - start_pos + 1
            if min_len > len_window: 
                min_len = len_window 
                start_pos_index = start_pos 
    return str[start_pos_index: start_pos_index + min_len]

>>> str1 = "asdaewsqgtwwsa"
>>> print(find_sub_string(str1))
daewsqgt
```
## 找到一个字符串中最短和最长的单词

Write a Python program to find smallest and largest word in a given string.

```python
>>> def smallest_largest_words(str1):
    word = "";
    all_words = [];
    str1 = str1 + " ";
    for i in range(0, len(str1)):
        if(str1[i] != ' '):
            word = word + str1[i];  
        else:
            all_words.append(word);  
            word = "";  
          
    small = large = all_words[0];  
   
#Find smallest and largest word in the str1  
    for k in range(0, len(all_words)):
        if(len(small) > len(all_words[k])):
            small = all_words[k];
        if(len(large) < len(all_words[k])):
            large = all_words[k];
    return small,large;

>>> 
>>> str1 = "Write a Java program to sort an array of given integers using Quick sort Algorithm.";
>>> small, large = smallest_largest_words(str1)
>>> print("Smallest word: " + small);
Smallest word: a
>>> print("Largest word: " + large);
Largest word: Algorithm.
```


