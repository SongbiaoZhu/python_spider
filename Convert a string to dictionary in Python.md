# Convert a string to dictionary in Python

[TOC]

We can use ast.literal_eval() here to evaluate the string as a python  expression. It safely evaluates an expression node or a string  containing a Python expression.The string or node provided may only  consist of the following Python literal structures: strings, numbers,  tuples, lists, dicts, booleans, and None. For example: 

```python
 >>>import ast
>>>x = ast.literal_eval("{'foo' : 'bar', 'hello' : 'world'}")
>>>type(x)
<type'dict'>
 
```

Dictionaries can also be seen as JSON strings. Thus we can use the json module to convert a string to dict as well. For example,

```python
 >>>import json
>>>x = json.loads("{'foo' : 'bar', 'hello' : 'world'}")
>>>type(x)
<type'dict'>
```

## 致谢

* [How to convert a string to dictionary in Python?](https://www.tutorialspoint.com/How-to-convert-a-string-to-dictionary-in-Python)