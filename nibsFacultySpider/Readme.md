# nibsFacultySpider_SOP

[TOC]

## Aims

Crawl the excellent PIs information.

Learn some lesson from their work experience.

Aim to be a excellent investigator like them.

## Workflow (Methods)

1. crawl all the faculty ID
2. crawl the href of every page,  get all the href of every faculty
3. crawl the information of every faculty.

```html
# page urls
http://www.nibs.ac.cn/yjsjyimg.php?cid=8&sid=25
http://www.nibs.ac.cn/yjsjyimg.php?cid=8&sid=25&page=2
http://www.nibs.ac.cn/yjsjyimg.php?cid=8&sid=25&page=3

# faculty information URLs
http://www.nibs.ac.cn/yjsjyimgshow.php?cid=8&sid=25&id=732
http://www.nibs.ac.cn/yjsjyimgshow.php?cid=8&sid=25&id=724
```

## Scripts

* nibsFacultySpiderExample.py

Use Prof. Luo page as example, try crawl the faculty information

* nibsFacultySpider.py

based on the above example, try crawl all the faculties information

* nibsFacultyWorkSpider.py

based on the above script, just crawl the  personal information, Education, Work experience. Leave out the Research interest and Publication list. The major difference located on lines 43-53.

## Results

Please look at the files with '_new.txt'

Faculty_new.txt

nibsFaculty_new.txt

nibsFacultyWork_new.txt