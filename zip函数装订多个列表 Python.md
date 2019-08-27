# zip函数装订多个列表 Python

[TOC]

In Python 2.x, you can just use [`zip`](http://docs.python.org/2/library/functions.html#zip):

```python
>>> t1 = ["abc","def","ghi"]
>>> t2 = [1,2,3]
>>> zip(t1, t2)
[('abc', 1), ('def', 2), ('ghi', 3)]
>>>
```

However, in Python 3.x, `zip` returns a zip object (which is an [iterator](http://docs.python.org/2.7/glossary.html#iterator)) instead of a list.  This means that you will have to explicitly convert the results into a list by putting them in [`list`](http://docs.python.org/3/library/functions.html#func-list):

```python
>>> t1 = ["abc","def","ghi"]
>>> t2 = [1,2,3]
>>> zip(t1, t2)
<zip object at 0x020C7DF0>
>>> list(zip(t1, t2))
[('abc', 1), ('def', 2), ('ghi', 3)]
>>>
```

## 致谢

* [stackoverflow](https://stackoverflow.com/questions/21684770/how-to-merge-two-lists-into-a-sequence-of-columns-in-python)