# 英文的月份转数字及数字转英文 Python

[TOC]

借助 calendar 模块可以很快实现转换。

## Code

```python
In [1]: import calendar
 
# 数字转月份的简写
In [2]: calendar.month_abbr[12]
Out[2]: 'Dec'
 
# 简写月份转数字
In [3]: list(calendar.month_abbr).index('Dec')
Out[3]: 12
 
# 数字转月份的全写
In [4]: calendar.month_name[12]
Out[4]: 'December'
 
# 月份转数字
In [5]: list(calendar.month_name).index('December')
Out[5]: 12

```

## 致谢

[csdn_blog](https://blog.csdn.net/u010891397/article/details/86632214)