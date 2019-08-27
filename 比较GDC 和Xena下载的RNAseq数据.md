# 比较GDC 和Xena下载的RNAseq数据

[TOC]

## 介绍GDC下载数据和整理数据的方法

选择TCGA-brca 的male样本为例，因为只有12个病人。

1. 下载Files选项卡下的JSON文件和TSV文件

* files.2019-05-28.json，该文件包含表达量数据txt文件的文件名和case id 的对应关系
* repository-files-table.2019-05-28.tsv，该文件用途不大，只包含表达量数据txt文件大小的一些信息



2. 下载Cases 选项卡下面的

* 

下载Cilinical 的TSV文件 clinical.cases_selection.2019-05-28.tar.gz；

下载manifest文件 gdc_manifest.2019-05-28.txt；

下载JSON文件 files.2019-05-28.json；



linux 解压.gz文件是用命令 tar zxvf clinical.cases_selection.2019-05-28.tar.gz



## 介绍GDC下载数据和整理数据的方法