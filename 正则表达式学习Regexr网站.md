# 正则表达式学习Regexr网站

[TOC]

## 工具网站

[Regexr](https://regexr.com/)

## example data

这里选用了uniprot网页的部分源代码数据

```html
<div class="blogfooter">
<dl>
<dt><strong>References</strong></dt>
<dd>1.	Block A.K., Vaughan M.M., Schmelz E.A., Christensen S.A.
<p> Biosynthesis and function of terpenoid defense compounds in maize (Zea mays)
<p> Planta 249:21-30(2019)
<p> PMID:<a href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&amp;db=pubmed&amp;dopt=Abstract&amp;list_uids=30187155&amp;query_hl=3&amp;itool=pubmed_docsum">30187155</a></dd>
<dd>2.	Tamiru A., Bruce T.J.A., Richter A., Woodcock S.M. et al.
<p> A maize landrace that emits defense volatiles in response to herbivore eggs possesses a strongly inducible terpene synthase gene
<p> Ecology and Evolution 7:2835-2845(2017)
<p> PMID:<a href="http://www.ncbi.nlm.nih.gov/entrez/query.fcgi?cmd=Retrieve&amp;db=pubmed&amp;dopt=Abstract&amp;list_uids=28428873&amp;query_hl=3&amp;itool=pubmed_docsum">28428873</a></dd>
</dl>
</div> 
```

## zhs write regex expressions

* 提取上述文献链接：`a href=".+"`
* 提取文献PMID号`>[0-9]{8}<`
* 提取文献发表的卷期和年份信息：`[0-9]+:[0-9]+-[0-9]+\([0-9]{4}\)`
* 提起文献发表的杂志名称：`<p>.+[0-9]:`，这一步不能到位，可以再进行去除筛选出来的字符串中的数字即可。

## 学习总结

* 这个网站十分方便，因为在讲text复制粘贴进去以后，可以动态地调整编写的regex表达式内容，实时查看匹配的效果是否符合预期。
* 所以该网站除了便于学习正则表达式，还可以为以后编写正则表达式提供帮助。
* 当正则表达式中需要输入(..)，就是匹配括号时，则需要对括号的每一部分加上转义字符，见上述提取文献发表的卷期和年份信息的例子。

