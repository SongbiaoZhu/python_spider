# time标准库 python

[TOC]

## Code

下面是一个示例，一个与 [**RFC 2822**](https://tools.ietf.org/html/rfc2822.html) Internet电子邮件标准以兼容的日期格式

```python
>>> from time import gmtime, strftime
>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'
```



## Acknowledgement

# [`time`](https://docs.python.org/zh-cn/3/library/time.html#module-time) 

- 参见

  - 模块 [`datetime`](https://docs.python.org/zh-cn/3/library/datetime.html#module-datetime)

    更多面向对象的日期和时间接口。 

  - 模块 [`locale`](https://docs.python.org/zh-cn/3/library/locale.html#module-locale)

    国际化服务。 区域设置会影响 [`strftime()`](https://docs.python.org/zh-cn/3/library/time.html#time.strftime) 和 [`strptime()`](https://docs.python.org/zh-cn/3/library/time.html#time.strptime)  中许多格式说明符的解析。 

  - 模块 [`calendar`](https://docs.python.org/zh-cn/3/library/calendar.html#module-calendar)

    一般日历相关功能。这个模块的 `timegm()` 是函数 [`gmtime()`](https://docs.python.org/zh-cn/3/library/time.html#time.gmtime) 的反函数。 