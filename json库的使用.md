# json库的使用

[TOC]

### 一、关于 json

json的简介直接引用百度百科的定义：

> JSON(JavaScript Object Notation, JS 对象简谱) 是一种轻量级的数据交换格式。它基于 ECMAScript (欧洲计算机协会制定的js规范)的一个子集，采用完全独立于编程语言的文本格式来存储和表示数据。简洁和清晰的层次结构使得 JSON 成为理想的数据交换语言。 易于人阅读和编写，同时也易于机器解析和生成，并有效地提升网络传输效率。

实际上 json的格式和 python中的字典很像，也是由键值对组成，但是 python中的值可以为任何对象（列表、字典、字符串、数字等等），而 json中的值只能是数组（列表）、字典、字符串、数组、布尔值中的一中或几种。

其格式就像下面这样：

注意：json中的引号必须是双引号，否则会报错

```json
{
    "key1": "value1",
    "key2": [1,2,"value2"],
    "key3": 
    {
        "key31": "value1",
        "key32": [1,2,"value2"],
        "key33": true,
    },
}
```

### 二、json库的使用

json库一共有三个方法，分别是 dump、dumps、load、loads。

其中 dump和 dumps是用来把把字典和数组转换为 json格式的，dump把转换结果直接写入文件，dumps返回字符串。

load和 loads是把 json格式的数据转换为字典格式，load直接从 json文件中读取数据并返回字典对象，loads把字符串形式的 json数据转换成字典格式。

下面讲讲这些方法的具体用法。

**1、dump和 dumps**

dump的函数原型是 `dump(obj, fp)` 第一个参数 obj是要转换的对象，第二个参数 fp是要写入数据的文件对象。

dumps的函数原型是 `dumps(obj)` 参数是要转换的对象

注意：如果要转换的对象里有中文字符的话，要把 ensure_ascii设置为 False否则中文会被编码为 ascii格式

```python
#-*- coding: utf-8 -*
import json


test = {
    "key1": "value1",
    "key2": [1,2,"value2"],
    "key3":
    {
        "key31": "value1",
        "key32": [1,2,"value2"],
        "key33": True,
        "key34": "测试",
    },
}

#没有设置 ensure_ascii为 False
with open('test.json', 'w', encoding='utf-8') as fp:
    json.dump(test, fp)
#设置了 ensure_ascii为 False
with open('test_no_ascii.json', 'w', encoding='utf-8') as fp:
    json.dump(test, fp, ensure_ascii=False)

#test.json的文件内容为：
#{... ... "key33": true, "key34": "\u6d4b\u8bd5"}}
#test_no_ascii.json的文件内容为：
#{... ... "key33": true, "key34": "测试"}}
#注意到 python中的 True转换成了 Javascript里的 true
#另外在打开文件的时候强烈建议用 encoding指定文件编码
#还需要注意文件的打开模式 w是写入，文件已存在的话就覆盖
#要追加写入的话记得用 a模式打开

test_string = json.dumps(test, ensure_ascii=False)
print(test_string)
```

打印结果：



![img](https:////upload-images.jianshu.io/upload_images/8516750-b526e0e0eeb46343.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)



**2、load和 loads**

load的函数原型是 `load(fp)` 参数 fp是要读取的文件对象

loads的函数原型是 `loads(string)` 参数 string是要转换成 python对象的 json字符串，通常用来将网页中的 json数据转换为 python对象

```python
#-*- coding: utf-8 -*
import json


#json格式的字符串
test_string = '{"key1": "value1", "key2": [1, 2, "value2"], "key3": {"key31": "value1", "key32": [1, 2, "value2"], "key33": true, "key34": "测试"}}'

#从之前保存的 test_no_ascii.json中读取 注意模式为 r
with open('test_no_ascii.json', 'r', encoding='utf-8') as fp:
    json_obj_from_file = json.load(fp)

json_obj_from_web = json.loads(test_string)

#打印两个返回结果的类型
print(type(json_obj_from_file))
print(type(json_obj_from_web))
#打印两个返回结果的内容
print(json_obj_from_file)
print(json_obj_from_web)
```

打印结果：



![img](https:////upload-images.jianshu.io/upload_images/8516750-a6d38380a795390d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1000)

## 致谢

* [python爬虫系列之数据的存储（一）：json库的使用](https://www.jianshu.com/p/0ba2b643c0f2)

* [JSON 编码和解码器](https://docs.python.org/zh-cn/3/library/json.html?highlight=json#module-json)