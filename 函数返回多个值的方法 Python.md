# 函数返回多个值的方法 Python

[TOC]

## 知识点

- 只执行第一条return语句

- 一条return语句中可以返回多个值，默认返回的是元组
- 可以加上[]，使返回的是列表
- 返回多个值时，可以用多个变量来对应接收多个返回值。

## code

```python
# 返回列表
>>> def test():
	a=11
	b=22
	c=33
	return [a,b,c]
 
>>> num=test()
>>> num
[11, 22, 33]

# 返回元组
>>> def test():
	a=11
	b=22
	c=33
	return a,b,c # same with 	return (a,b,c)
 
>>> num=test()
>>> num
(11, 22, 33)
```



## 致谢

* [csdn_blog](https://blog.csdn.net/panda996/article/details/84786649)
* 