# 函数传入不定个数参数 python

[TOC]

## 不定个数求和

```python
def add_2_int(a1, a2):
    return a1+a2

def add_int(*a):
    s = 0
    for e in a:
        s += e    
    return s

print(add_int(1, 2))
print(add_int(1, 2, 3))
```

* 在函数定义阶段使用`*`来打包，使得函数能接受任意多的入口参数个数。

* 这里调用`add_int`时输入参数是三个：`1,2,3`，但给`add_int`定义的输入是`*a`，那`*`的作用到底是什么呢？其实就是在调用函数时，把输入的三个参数`1,2,3`打包成一个元组(tuple)，即打包成`(1,2,3)`给`a`这个参数。

## 致谢

[csdn_blog](https://blog.csdn.net/u012102306/article/details/52250028)