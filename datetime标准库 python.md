# datetime标准库 python

[TOC]
## Index

- [有效的类型](https://docs.python.org/zh-cn/3/library/datetime.html#available-types)
- [`timedelta` 类对象](https://docs.python.org/zh-cn/3/library/datetime.html#timedelta-objects)
- [`date` 对象](https://docs.python.org/zh-cn/3/library/datetime.html#date-objects)
- [`datetime` 对象](https://docs.python.org/zh-cn/3/library/datetime.html#datetime-objects)
- [`time` Objects](https://docs.python.org/zh-cn/3/library/datetime.html#time-objects)
- [`tzinfo` 对象](https://docs.python.org/zh-cn/3/library/datetime.html#tzinfo-objects)
- [`timezone` Objects](https://docs.python.org/zh-cn/3/library/datetime.html#timezone-objects)
- [`strftime()` and `strptime()` Behavior](https://docs.python.org/zh-cn/3/library/datetime.html#strftime-and-strptime-behavior)

## Code

Examples of working with datetime objects:

```python
>>> from datetime import datetime, date, time
>>> # Using datetime.combine()
>>> d = date(2005, 7, 14)
>>> t = time(12, 30)
>>> datetime.combine(d, t)
datetime.datetime(2005, 7, 14, 12, 30)
>>> # Using datetime.now() or datetime.utcnow()
>>> datetime.now()   
datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)   # GMT +1
>>> datetime.utcnow()   
datetime.datetime(2007, 12, 6, 15, 29, 43, 79060)
>>> # Using datetime.strptime()
>>> dt = datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
>>> dt
datetime.datetime(2006, 11, 21, 16, 30)
>>> # Using datetime.timetuple() to get tuple of all attributes
>>> tt = dt.timetuple()
>>> for it in tt:   
...     print(it)
...
2006    # year
11      # month
21      # day
16      # hour
30      # minute
0       # second
1       # weekday (0 = Monday)
325     # number of days since 1st January
-1      # dst - method tzinfo.dst() returned None
>>> # Date in ISO format
>>> ic = dt.isocalendar()
>>> for it in ic:   
...     print(it)
...
2006    # ISO year
47      # ISO week
2       # ISO weekday
>>> # Formatting datetime
>>> dt.strftime("%A, %d. %B %Y %I:%M%p")
'Tuesday, 21. November 2006 04:30PM'
>>> 'The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}.'.format(dt, "day", "month", "time")
'The day is 21, the month is November, the time is 04:30PM.'

```

## `strftime()` and `strptime()` Behavior

[`date`](https://docs.python.org/zh-cn/3/library/datetime.html#datetime.date), [`datetime`](https://docs.python.org/zh-cn/3/library/datetime.html#datetime.datetime), and [`time`](https://docs.python.org/zh-cn/3/library/datetime.html#datetime.time) objects all support a `strftime(format)` method, to create a string representing the time under the control of an explicit format string. 

## Acknowledgement

# [`datetime`](https://docs.python.org/zh-cn/3/library/datetime.html#module-datetime)