# ggThemeAssist：调整主题并返回代码

R语言中的ggplot2是最美的绘图包之一。但调整主题的细节，需要写大量代码，而且反复修改、预览，费时费力。

当然你可以用Adobe Illustrator等工具进行后期编辑，但要是图重画，所有后期编辑的工作又要重来，无法实现可重复分析，每个修改都很崩溃。

有没有更方便的方式调整主题细节呢？

ggThemeAssist横空出事，它依赖shiny  (>= 0.13), miniUI (>= 0.1.1), rstudioapi (>= 0.5), ggplot2,  formatR，可以对ggplot2图形结果直接修改，并实时预览效果，同时编辑结束返回代码。相当于一个帮你写代码的翻译官！

此包必须在Rstudio环境中使用，运行下面代码：

```
# install.packages("ggThemeAssist")
library(ggplot2)
library(ggThemeAssist)
# 使用mtcars生成一个点图示例
gg <- ggplot(mtcars, aes(x = hp, y = mpg, colour = as.factor(cyl))) + geom_point()
# 开始调整主题
ggThemeAssistGadget(gg)
```

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/0.png)

看到打开了一个窗口，上部为图形预览窗口，下部有6个选项卡，分别对应各类主题细节的调整，下面我们进行详细解释。

## 1. 设置 Settings

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/1.png)

- 绘图维度 Plot dimensions

Width、Height可鼠标点击数值文本框右侧箭头微调图片宽、高尺寸，也可直接修改数字。

- 通用选项 General options

**Use FormatR 选项**可以格式化输出的R代码更具可读性，这可是R界大神，统计之都和R语言大会创始人谢益辉写的包。

默认勾选时，输出代码示例格式：

```
gg + theme(panel.background = element_rect(fill = NA), 
     plot.background = element_rect(fill = NA))
```

不勾选，编辑后返回代码格式如下：

```
gg + theme(panel.background = element_rect(fill  =  NA), plot.background = element_rect(fill  =  NA))
```

默认选项更利用阅读，但占用多行。选择全凭个人喜好，推荐勾选，可实现多行并缩进排版，方便阅读和同行交流。

**Multiline results 选项**是输出绘图代码一行行独立累加主题实现，还是行相加所有参数实现。

默认格式，不勾选多行，推荐，示例如下：

```
gg + theme(panel.grid.major = element_line(linetype = "solid"), 
    panel.grid.minor = element_line(linetype = "solid"), 
    plot.background = element_rect(linetype = "blank"))
```

勾选多行格式，示例如下，此种方案方便累加和后退去除参数，但变量多次重复出现，各有利弊：

```
gg <- gg + theme(panel.grid.major = element_line(linetype  =  'dashed'))
gg <- gg + theme(panel.grid.minor = element_line(linetype  =  'dashed'))
gg <- gg + theme(panel.background = element_rect(fill  =  'gray87'))
```

## 2. 面板和背景 Panel & Backgroud

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/2.png)

- 绘图区背景 Plot Background

即整个作图区的背景，包括填充色Fill，外边框类型Type、线宽Size和颜色Colour

- 面板背景 Panel Backgroud

即坐标轴围成的数据分布区域，属性同上，包括填充色Fill，外边框类型Type、线宽Size和颜色Colour

- 主网格 Grid Major

即图中X、Y轴刻度线对应的网格，建议使用，方便辅助识别数据位置；

- 次网格 Grid Minor

即图中X、Y轴刻度线间的补充网格，看具体情况使用，方便进一步辅助识别数据准确位置；

## 3. 坐标轴 Axis

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/31.png)

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/32.png)

- 坐标轴文字 Axis text

Family：字体家族，默认为Sans，和我们常用的Arial类似；还常用Courier系列等宽字体，如显示核酸、蛋白序列对齐要求时使用；Helvetica是Science杂志推荐字体；

Face: 字体样式，如标准 plain(Adobe系列软件称Regular)、加粗 bold、斜体 italic、粗斜体 bold.italic

Size：字体大小，推荐8(无纸质版在线网络杂志，如Nature  Communication、Communication Biology、Scientific  Report等)；可选7，适合Nature、Science最终发表字体大小；最小不要小于5，否则看不清。

Colour：颜色，默认为30%灰度 gray30，想突出坐标同刻度数值，可选black或gray0；

Hjust：X轴刻度值水平位置调整，默认0.5为相对刻度线居中对齐，0为刻度线左对齐；1为刻度线右对齐

Vjust：Y轴刻度值垂直位置调整，默认0.5为相对刻度线居中对齐，0为刻度线下对齐；1为刻度线上对齐

Angle：坐标轴角度，如标签过长，可调为30度或45度旋转避免文字重叠且节约空间，一般要配合Hjust为1右对齐才更美观；一般情况下要对x或y轴单独修改

- 坐标轴x文字属性 Axis text.x

默认可不修改，自动继承Axis text的属性。仅用于x轴属性需单独设置时修改，解释同上

- 坐标轴y文字属性 Axis text.y

默认可不修改，自动继承Axis text的属性。仅用于y轴属性需单独设置时修改，解释同上

- 坐标轴线属性 Axis line

主要修改X/Y轴的线型Type、宽度Size和颜色Colour

- 刻度线 Axis ticks

同坐标轴线，可修改X/Y轴的线型Type、宽度Size和颜色Colour

## 4. 标题与标签 Title and label

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/41.png)

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/42.png)

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/43.png)

- 标签 Lable

Title：图表标题，直接输入即可，方便吧

x-Axis label: 添加X轴标签

y-Axis label: 添加y轴标签

Colour：图例标题

Fill label：填充色标签

Size label：点大小标签

Alpha label：透明度标签

Linetype label：线型标签

Shape label：形状标签

- 标题属性 Plot Title

与坐标轴属性类似，详见前面“坐标轴文字 Axis text”说明

Family：字体家族

Face: 字体样式，如标准plain、加粗bold、任何italic、粗斜体bold.italic

Size：字体大小，标题可以使用12，即标准字体系1.5倍，并加粗

Colour：颜色

Hjust：沿X轴水平位置调整

Vjust：沿Y轴垂直位置调整

Angle：文字旋转角度，逆时针

- 坐标轴标签属性 Axis Labels

解释同上

## 5. 图例 Legend

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/5.png)

- 图例位置 Legend position

Position：位置，可选无none，左left，右right，上top，下buttom，图中XY

Direction：方向，可按水平horizontal，或垂直vertical排列

- 图例标题属性 Legend Title

Family：字体家族

Face: 字体样式

Size：字体大小，可调8-10，个人喜欢和坐标轴同样大小，有人喜欢大点

Colour：颜色

- 图例文字属性 Legend Text

同上

- 图例背景属性 Legend Background

括填充色Fill，外边框类型Type、线宽Size和颜色Colour

- 图例核心属性 Legend Keys

即图例中颜色图状的属性，同上

## 6. 子标题和图注 Subtitle and Caption

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/61.png)

![image](http://bailab.genetics.ac.cn/Note/R/ggThemeAssist/62.png)

可以修改子标题(Subtitle)和图注(Caption)中的内容。同时可修改文字的属性，如字体家族、样式、大小、颜色和水平位置

## 7. 编辑结果导出绘图代码

以上面板中可修改上百个参数，并提供几百个属性值的选择。这些要是靠自己记住，那可真是太难了。此包为R语言绘图的细节调提供了极大帮助。

而且调好的样式，点击done完成，马上写书规范的代码就写好了，方便可重复计算和进一步修改。这就是代码的强大之处。

```
gg + theme(plot.subtitle = element_text(size = 8, 
    colour = "gray25", hjust = 0.25), axis.line = element_line(linetype = "dotdash"), 
    panel.grid.minor = element_line(colour = "gray95", 
        linetype = "dotted"), axis.text = element_text(size = 8, 
        face = "bold", colour = "black", 
        hjust = 1), axis.text.x = element_text(size = 1, 
        angle = 45), legend.key = element_rect(fill = "antiquewhite4"), 
    legend.background = element_rect(fill = "gray93", 
        colour = "antiquewhite4", size = 1, 
        linetype = "solid")) +labs(title = "Title for figure ", x = "x-Axis label", 
    colour = "汽纲数量", fill = "fill title", 
    subtitle = "Subtitle")
```

注意：在使用中最好不要用中文，否则会出现缺失引号代码无法运行的情况，自己手动添加引号括上中文即可运行。

以上展示过程的R环境信息

```
> sessionInfo()
R version 3.6.0 (2019-04-26)
Platform: x86_64-w64-mingw32/x64 (64-bit)
Running under: Windows 10 x64 (build 17134)

Matrix products: default

locale:
[1] LC_COLLATE=Chinese (Simplified)_China.936  LC_CTYPE=Chinese (Simplified)_China.936   
[3] LC_MONETARY=Chinese (Simplified)_China.936 LC_NUMERIC=C                              
[5] LC_TIME=Chinese (Simplified)_China.936    

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

other attached packages:
[1] shiny_1.3.2         ggThemeAssist_0.1.5 ggplot2_3.1.1      

loaded via a namespace (and not attached):
 [1] Rcpp_1.0.1        pillar_1.4.1      compiler_3.6.0    formatR_1.7       later_0.8.0       plyr_1.8.4        tools_3.6.0      
 [8] digest_0.6.19     jsonlite_1.6      tibble_2.1.3      gtable_0.3.0      pkgconfig_2.0.2   rlang_0.3.4       cli_1.1.0        
[15] rstudioapi_0.10   withr_2.1.2       dplyr_0.8.1       grid_3.6.0        tidyselect_0.2.5  glue_1.3.1        R6_2.4.0         
[22] sessioninfo_1.1.1 purrr_0.3.2       magrittr_1.5      scales_1.0.0      promises_1.0.1    htmltools_0.3.6   assertthat_0.2.1 
[29] mime_0.6          colorspace_1.4-1  xtable_1.8-4      httpuv_1.5.1      labeling_0.3      miniUI_0.1.1.1    lazyeval_0.2.2   
[36] munsell_0.5.0     crayon_1.3.4     
```