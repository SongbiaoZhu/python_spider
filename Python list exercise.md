# list exercise Python

[TOC]

## 克隆或复制一个列表

* Write a Python program to clone or copy a list.

```python
>>> oldlist = [1,2,3,4,5,4,3,2,1]
>>> newlist = list(oldlist)
>>> print(newlist)
[1, 2, 3, 4, 5, 4, 3, 2, 1]
>>> print(oldlist)
[1, 2, 3, 4, 5, 4, 3, 2, 1]
```
## 移除列表中重复元素

* Write a Python program to remove duplicates from a list.

```python
>>> a = [1,2,3,4,1,2,3,4,5]
>>> l = list(set(a))
>>> l
[1, 2, 3, 4, 5]
```
## 对元组为元素的列表，按照元组最后一个值对列表排序

* Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.

```python
>>> def last(n): return n[-1]

>>> def sort_list_last(tuples):
	return sorted(tuples, key = last)

>>> print(sort_list_last([(2,5),(1,2),(4,4),(2,3),(2,1)]))
[(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
```
## 移除一个列表特定几个index位置的元素

* Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

```python
>>> color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
>>> color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
>>> print(color)
['Green', 'White', 'Black']
```
## 判断列表1和列表2是否至少有一个相同元素

* Write a Python function that takes two lists and returns True if they have at least one common member.

```python
# zhs write
>>> def common(list1,list2):
	set12 = set(list1+list2)
	if len(set12) == (len(list1)+len(list2)):
		return False
	else:
		return True

	
>>> common([1,2,3,4,5],[6,7,8,9,10])
False
>>> common([1,2,3,4,5],[6,7,8,9,10,1])
True

>>> def common_data(list1, list2):
     result = False
     for x in list1:
         for y in list2:
             if x == y:
                 result = True
                 return result

                
>>> print(common_data([1,2,3,4,5], [5,6,7,8,9]))
True
>>> print(common_data([1,2,3,4,5], [6,7,8,9]))
None
```
## 移除list中的奇数元素

* Write a Python program to print the numbers of a specified list after removing even numbers from it.

```python
>>> num = [7,8, 120, 25, 44, 20, 27]
>>> num = [x for x in num if x%2!=0]
>>> print(num)
[7, 25, 27]
```
## 列出一个列表所有元素的所有可能排列的列表

* Write a Python program to generate all permutations of a list in Python.

```python
>>> import itertools
>>> print(list(itertools.permutations([1,2,3])))
[(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```
## 获得两个列表的不同元素

* Write a Python program to get the difference between the two lists.

```python
>>> l1 = [1,2,3,4]
>>> l2 = [2,3,4]
>>> print(list(set(l1)-set(l2)))
[1]
```
## 获得一个列表的index 和value

* Write a Python program access the index of a list.

```python
>>> num = [11,14,35,46,45,24]
>>> for num_index, num_val in enumerate(num):
	print(num_index, num_val)

	
0 11
1 14
2 35
3 46
4 45
5 24
```
## 随机从列表中选择一个元素

* Write a Python program to select an item randomly from a list.

```python
>>> import random
>>> l = [1,2,3,4,5,7,6,4,3,2]
>>> print(random.choice(l))
3
>>> print(random.choice(l))
2
```
## 找到列表中一个元素的index

* Write a Python program to find the index of an item in a specified list.

```python
>>> x = [1,2,3]
>>> print(x.index(2))
1
```
## 将嵌套列表转化成单一列表

* Write a Python program to flatten a shallow list.

```python
>>> l1 = [[1,2,3],['a','b','c']]
>>> x = []
>>> for i in range(len(l1)):
	x+=[x for x in l1[i]]

	
>>> x
[1, 2, 3, 'a', 'b', 'c']
```
## 将列表中元素转化成一个字符串

* Write a Python program to convert a list of characters into a string.

```python
>>> s = ['a', 'b', 'c', 'd']
>>> str1 = ''.join(s)
>>> print(str1)
abcd
```
## 统计列表中所有元素的出现频率

* Write a Python program to get the frequency of the elements in a list.

```python
>>> import collections
>>> my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
>>> ctr = collections.Counter(my_list)
>>> print(ctr)
Counter({10: 4, 20: 4, 40: 2, 50: 2, 30: 1})
```
## 判断两个列表中的元素是否是环性相等

* Write a python program to check whether two lists are circularly identical.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-26.png)

```python
>>> list1 = [10, 10, 0, 0, 10]
>>> list2 = [10, 10, 10, 0, 0]
>>> list3 = [1, 10, 10, 0, 0]
>>> print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))
True
>>> print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2)))
False

# zhs notes:这里的判断是否环形相等的根据是，判断第2个列表元素组成的字符串是否在2倍的第1个列表中元素组成的字符串之中。
# 而map函数，就是将一个function 对一个迭代对象的每一个对象进行应用，因为list1中的元素是数字，不能直接连接，所以通过map函数将每个元素转化为str。
```
## 对列表的每一个元素添加一个1-n的后缀

* Write a Python program to create a list by concatenating a given list which range goes from 1 to n.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-35.png)

```python
>>> my_list = ['p', 'q']
>>> n = 4
>>> new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
>>> print(new_list)
['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4']
```
## 检查一个列表是否是另外一个列表的子列表

* Write a Python program to check whether a list contains a sublist.

```python
>>> def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set

>>> a = [2,4,3,5,7]
>>> b = [4,3]
>>> c = [3,7]
>>> print(is_Sublist(a, b))
True
>>> print(is_Sublist(a, c))
False
```
## 生成一个list，其中每个元素是连续的五个整数

* Write a Python program to generate groups of five consecutive numbers in a list.

```python
>>> l = [[5*i + j for j in range(1,6)] for i in range(5)]
>>> print(l)
[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
```
## 找出两个列表中彼此不同的元素

* Write a Python program to find missing and additional values in two lists.

```python
>>> list1 = ['a','b','c','d','e','f']
>>> list2 = ['d','e','f','g','h']
>>> set(list1).difference(list2)
{'a', 'c', 'b'}
>>> set(list2).difference(list1)
{'g', 'h'}
```
## 一次性常见多个列表

* Write a Python program to create multiple lists.

```python
>>> obj = {}
>>> for i in range(1,21):
	obj[str(i)] = []

	
>>> obj['1']
[]
>>> i
20
>>> obj[str(i)]
[]
# zhs notes:如此可以实现在迭代中每次使用不同的列表储存数据
```
## 将list中的多个整数元素合并成一个整数

* Write a Python program to convert a list of multiple integers into a single integer.

```python
>>> L = [11, 33, 50]
>>> x = int("".join(map(str, L)))
>>> x
113350
```
## 将列表中的元素两两交换顺序

* Write a Python program to change the position of every n-th value with the (n+1)th in a list. 

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-38.png)

```python
>>> from itertools import zip_longest, chain, tee
>>> def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))

>>> n = [0,1,2,3,4,5]
>>> print(replace2copy(n))
[1, 0, 3, 2, 5, 4]
```
## 找到两个列表中相同的元素

* Write a Python program to find common items from two lists. 

```python
>>> color1 = "Red", "Green", "Orange", "White"
>>> color2 = "Black", "Green", "White", "Pink"
>>> print(set(color1) & set(color2))
{'Green', 'White'}
```
## 以元组为元素的列表，获取其所有唯一值组成一个新列表

* Write a Python program to convert a pair of values into a sorted unique array.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-45.png)

```python
>>> L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]
>>> print("Sorted Unique Data:",sorted(set().union(*L)))
Sorted Unique Data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# zhs notes: set.union()的用法
```
`set.union(set1, set2...)`, 返回两个集合的并集。[set.union](https://www.runoob.com/python3/ref-set-union.html)

## 在列表中每个元素前插入一个元素

* Write a Python program to insert an element before each element of a list.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-47.png)

```python
>>> color = ['Red', 'Green', 'Black']
>>> color = [v for elt in color for v in ('c', elt)]
>>> print(color)
['c', 'Red', 'c', 'Green', 'c', 'Black']
```
## 逐行打印嵌套列表中的每一个子列表元素

* Write a Python program to print a nested lists (each list on a new line) using the print() function.

```python
>>> colors = [['Red'], ['Green'], ['Black']]
>>> print('\n'.join([str(lst) for lst in colors]))
['Red']
['Green']
['Black']
```
## 将两个列表分别作为键和值组成字典

* Write a Python program to convert list to list of dictionaries.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-49.png)

```python
>>> color_name = ["Black", "Red", "Maroon", "Yellow"]
>>> color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
>>> print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])
[{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

# zhs notes：用到了zip函数，然后再使用了列表解析式。
```
## 对嵌套字典组成的列表按照字典元素进行排序列表

* Write a Python program to sort a list of nested dictionaries.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-50.png)

```python
>>> my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
>>> my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
>>> print(my_list)
[{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]

```
## 按照每n个元素分割一个list为多个list

* Write a Python program to split a list every Nth element.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-51.png)

```python
# zhs write
>>> C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
>>> def list_slice2(list1,step):
	sublist1 = []
	sublist2 = []
	sublist3 = []
	for i, value in enumerate(list1):
		if i %3 ==0:
			sublist1.append(value)
		elif i %3 ==1:
			sublist2.append(value)
		elif i %3 ==2:
			sublist3.append(value)
	return [sublist1,sublist2,sublist3]

>>> print(list_slice2(C,3))
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

# a better solution
>>> def list_slice(S, step):
    return [S[i::step] for i in range(step)]

>>> print(list_slice(C,3))
[['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]
#上述所使用的方法就是对一个列表从一个位置起始按照一个步长到结尾来提取元素，举例如下
>>> print([C[0::3]])
[['a', 'd', 'g', 'j', 'm']]
>>> print([C[1::3]])
[['b', 'e', 'h', 'k', 'n']]
>>> print([C[2::3]])
[['c', 'f', 'i', 'l']]
```
## 以字典为元素的列表，移除每个元素中某一个key的字典

* Write a Python program to remove key values pairs from a list of dictionaries.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-55.png)

```python
>>> original_list = [{'key1':'value1', 'key2':'value2'}, {'key1':'value3', 'key2':'value4'}]
>>> new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]
>>> print(new_list)
[{'key2': 'value2'}, {'key2': 'value4'}]
# zhs notes:这也是一个嵌套使用列表解析式的例子。这里把每一个dic就是作为一个列表元素对待的。
```
## 去除以列表为元素的列表中的重复元素

* Write a Python program to remove duplicates from a list of lists.

```python
>>> import itertools
>>> num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
>>> num.sort()
>>> print(num)
[[10, 20], [10, 20], [30, 56, 25], [33], [40], [40]]
>>> new_num = list(num for num,_ in itertools.groupby(num))
>>> print("New List", new_num)
New List [[10, 20], [30, 56, 25], [33], [40]]
```
## 获得一个字典的深度层级

* Write a Python program to get the depth of a dictionary.

```python
>>> def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0

>>> dic = {'a':1, 'b': {'c': {'d': {}}}}
>>> print(dict_depth(dic))
4
```
## 检查一个字典为元素的列表中是否每一个字典都是空

* Write a Python program to check if all dictionaries in a list are empty or not.
* all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否都为 TRUE，如果是返回 True，否则返回 False。元素除了是 0、空、None、False 外都算 True。

```python
>>> my_list = [{},{},{}]
>>> my_list1 = [{1,2},{},{}]
>>> print(all(not d for d in my_list))
True
>>> print(all(not d for d in my_list1))
False
```
## 检查一个列表中是否是每一个元素都等于某一值

* Write a Python program to check if all items of a list is equal to a given string.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-57.png)

```python
>>> color1 = ["green", "orange", "black", "white"]
>>> color2 = ["green", "green", "green", "green"]
>>> print(all(c == 'blue' for c in color1))
False
>>> print(all(c == 'green' for c in color2))
True
```

## 检查一个列表中的每一个元素是否都大于某一值

* Write a Python program to find all the values in a list are greater than a specified number.

```python
>>> list1 = [220, 330, 500]
>>> print(all(x >= 200 for x in list1))
True
```



## 将一个列表样的字符串转换成列表

* Write a Python program to convert a string to a list.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-56.png)

```python
>>> import ast
>>> color ="['Red', 'Green', 'White']"
>>> print(ast.literal_eval(color))
['Red', 'Green', 'White']
```
## 将列表1最后一个元素用列表2替换

* Write a Python program to replace the last element in a list with another list.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-58.png)

```python
>>> num1 = [1, 3, 5, 7, 9, 10]
>>> num2 = [2, 4, 6, 8]
>>> num1[-1:] = num2
>>> print(num1)
[1, 3, 5, 7, 9, 2, 4, 6, 8]
# other use
>>> num1[0:] = num2
>>> print(num1)
[2, 4, 6, 8]
>>> num1[:0] = num2
>>> print(num1)
[2, 4, 6, 8, 2, 4, 6, 8]
```
## 创建n个空字典组成的列表

* Write a Python program to create a list of empty dictionaries.

```python
>>> n = 5
>>> l = [{} for _ in range(n)]
>>> print(l)
[{}, {}, {}, {}, {}]
# zhs notes：同理可以创建n个空列表组成的列表
```
## python

* Write a Python program to insert a given string at the beginning of all items in a list.

![](https://www.w3resource.com/w3r_images/Python-data-type-list-excercise-63.png)

```python
>>> num = [1,2,3,4]
>>> print(['emp{0}'.format(i) for i in  num])
['emp1', 'emp2', 'emp3', 'emp4']
```
## 同时在两个列表中进行迭代

* Write a Python program to iterate over two lists simultaneously.

```python
>>> num = [1, 2, 3]
>>> color = ['red', 'white', 'black']
>>> for (a,b) in zip(num, color):
     print(a, b)

     
1 red
2 white
3 black
```
## 通过index获得字典中的keys值

* Write a Python program to access dictionary key’s element by index.

```python
>>> num = {'physics': 80, 'math': 90, 'chemistry': 86}
>>> print(list(num)[0])
physics
>>> print(list(num)[1])
math
>>> print(list(num)[2])
chemistry
```
## 找到以列表为元素的嵌套列表中，元素和最大的元素

* Write a Python program to find the list in a list of lists whose sum of elements is the highest.

```python
>>> num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
>>> print(max(num, key=sum))
[10, 11, 12]
```

