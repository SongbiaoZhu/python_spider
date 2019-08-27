# Write Text to a File in Python

[TOC]

## code

* Writing One Line at a Time to a File in Python Using write()

```python
textList = ["One", "Two", "Three", "Four", "Five"]

outF = open("myOutFile.txt", "w")
for line in textList:
  # write line to output file
  outF.write(line)
  outF.write("\n")
outF.close()
```

* Writing One Line at a Time to a File in Python Using “print”. Instead of printing a statement to the screen, we redirect to the output file object.

```python
outF = open("myOutFile.txt", "w")
for line in textList:
  print >>outF, line
outF.close()
```

* writelines(): Writing All The Lines at a Time to a File in Python. For example to write our list of all line “all_lines”, using “writelines().

```python
outF = open("myOutFile.txt", "w")
outF.writelines(all_lines)
outF.close()
```

* We can also make our lives easier without writing file.close() statement by using [with statement](http://cmdlinetips.com/2016/01/opening-a-file-in-python-using-with-statement) to write to a file. For example,

```python
with open(out_filename, 'w') as out_file:
     .. 
     .. 
     .. parsed_line
     out_file.write(parsed_line)
```



## 致谢

* [3 Ways to Write Text to a File in Python](https://cmdlinetips.com/2012/09/three-ways-to-write-text-to-a-file-in-python/)
* [3 Ways to Read A Text File Line by Line in Python](http://cmdlinetips.com/2011/08/three-ways-to-read-a-text-file-line-by-line-in-python/)