# ImageJ分析细胞划痕面积

[TOC]

## 原理

细胞划痕实验是目前测定细胞迁移运动与修复能力的最常用也是最简单的方法，基本原理是：在融合的单层细胞上人为制造一个空白区域，称为“划痕/伤口”，边缘的细胞会逐渐进入空白区域使“划痕/伤口”愈合。因其类似体外伤口愈合过程，又名伤口愈合实验（Wound-Healing  Assay），广泛用于可以观察药物、基因等外源因素对细胞迁移和修复的影响。

 

**原理：**如下图所示：

![细胞迁移动态图](http://www.bio-review.com/wp-content/uploads/2018/10/1webp.gif)

## 实验过程

在体外培养皿或平板培养的单层贴壁细胞上，用微量枪头或其它硬物在细胞生长的中央区域划线，去除中央部分的细胞，然后再继续培养细胞至实验设定的时间（可有不同时间点），取出细胞培养板，显微镜下观察周边细胞是否迁至中央划痕区，并拍照。

## ImageJ分析细胞划痕面积

那么如何在ImageJ中实现上图划痕面积和伤口愈合百分比的分析呢？这时候ImageJ就可以派上大用场，ImageJ这个图像分析大杀器，让实验结果所暗藏的规律清晰明了地呈现你的面前。

 

我们只需统计划痕面积（Scratch Area）随着时间的变化率以及伤口愈合百分比（Wound healing percentage），即可对细胞的侵袭性了如指掌。下面看详细步骤：

### **步骤一**：open图片

打开ImageJ软件，其界面：File，Open，选择待分析图片（图一），界面如下：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/3.webp_.jpg)

### **步骤二**：Image--Process

#### 转换8-bit：Image--Type--8-bit

#### 增强对比：Process，Enhance Contrast，出现如界面：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/2.webp_.jpg)

勾上Normalize，Saturated pixels：0.3%，点击OK，效果如下：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/3.webp_.jpg)

#### 平滑处理：Process，Smooth（平滑），效果如下：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/4.webp_.jpg)

#### 寻找边缘：Process，Find Edges（寻找边缘），效果如下：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/5.webp_.jpg)


### **步骤三**：Image--Adjust--Threshold

Image，Adjust，Threshold，阈值选定，选中为红色，调节阈值为0—20。点击Apply。

![img](http://www.bio-review.com/wp-content/uploads/2018/10/6.webp_.jpg)

效果如下：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/7.webp_.jpg)

### **步骤四**：魔棒选择划痕区域并测量面积

选择魔棒工具，魔棒工具位于下图右下角：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/8.webp_.jpg)

点击黑色的划痕部分，效果如下：

![img](http://www.bio-review.com/wp-content/uploads/2018/10/9.webp_.jpg)

点击Analyze，Measure，结果如下，划痕面积Area为43328平方像素。根据最开始的划痕面积，跟某一时间愈合的那一部分面积（最开始面积-某时间点的面积）与最初面积的比值即可得到伤口愈合的百分比。

由此我们得到了划痕面积（Scratch Area）随着时间的变化、伤口愈合百分比（Wound healing percentage），进行后续统计分析即可。

![img](http://www.bio-review.com/wp-content/uploads/2018/10/10.webp_.jpg)