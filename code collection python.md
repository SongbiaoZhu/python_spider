# code collection python

[TOC]

## 获取最近的一个周四的日期

```python
def getLateThu():
    '''
    get the last thursday and check the thursday in issueDates
    '''
    today = datetime.date.today()
    m4 = calendar.THURSDAY
    oneday = datetime.timedelta(days = 1)
    while today.weekday() !=m4:
        today -=oneday
    return today
```

## 获取从某一日期开始间隔固定天数的所有日期

```python
def getIssueDates():
    '''
    get the all the issue dates from 2010.1.8 to 2050.12.31
    '''
    start = datetime.date(2010,1,8)
    end = datetime.date(2051,1,1)
    issDates = [start]
    oneday = datetime.timedelta(days = 1)
    while start < end:
        start += oneday * 14
        issDates.append(start)
    return issDates
```

## writelines()报错‘gbk’ codec can’t encode character ‘\xa0’的问题解决办法

```python
# 在Python中将网址写入文件的时候，会碰到：UnicodeEncodeError: ‘gbk’ codec can’t encode character ‘\xa0’ in position 0这个问题。
# 其实就是在windows中，新建的文本文件的默认编码是gbk.
# 如此,我们可以在程序中提前指定编码就可以了. 而utf-8通用,就选它了 …….

f = open(‘a.txt’, ‘w’,encoding=’utf-8’)
```

[解决UnicodeEncodeError: 'gbk' codec can't encode character '\xa0' in position 0问题](https://www.e-learn.cn/content/qita/1105857)

## 多变量的for循环 详解

```python
n = 9
      
for i, j in zip(range(n-1, 0, -1), range(n//2)):
    print ('i = {0}, j = {1} '.format(i, j))
    
print(list(zip(range(n-1, 0, -1), range(n//2))))
```

