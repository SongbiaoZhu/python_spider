# writelines and write Python

[TOC]

# write和writelines的区别

* file.write(str)的参数是一个字符串，就是你要写入文件的内容.`write` expects a single string. 

* file.writelines(sequence)的参数是序列，比如列表，它会迭代帮你写入文件。`writelines` expects an iterable of strings. (an iterable object can be a tuple, a list, a string, or an iterator in the most general sense). Each item contained in the iterator is expected to be a string.

## Code

```python
lines = ['line1', 'line2']
with open('filename.txt', 'w') as f:
    f.write('\n'.join(lines))
# The construct '\n'.join(lines) concatenates (connects) the strings in the list lines and uses the character '\n' as glue. It is more efficient than using the + operator.  

# Starting from the same lines sequence, ending up with the same output, but using writelines():
lines = ['line1', 'line2']
with open('filename.txt', 'w') as f:
    f.writelines("%s\n" % l for l in lines)
# This makes use of a generator expression and dynamically creates newline-terminated strings. writelines() iterates over this sequence of strings and writes every item.
    
```

## 致谢

* [Python - write() versus writelines() and concatenated strings](https://stackoverflow.com/questions/12377473/python-write-versus-writelines-and-concatenated-strings)

