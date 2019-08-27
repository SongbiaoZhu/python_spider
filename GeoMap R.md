# 数据热图的地图显示

R语言绘制数据地图.

[TOC]

## 该代码能做什么？

**各省份热力地图** 
![](http://mmbiz.qpic.cn/mmbiz/x2S0icdguVdibBkM5NnXicc6I05ous4nJ9w6icceicLBXP75Owx8qEXoGKgcicrRbrYWVJfiazwhR3YhNPqIMt0dGrNjA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1).

**某省各市热力地图**
![](http://mmbiz.qpic.cn/mmbiz/x2S0icdguVd9EmXQ7g6vkmb3zYIYOGiaiaHJaotHEusYgIz5ehSExMDgelViaxGNjvFfkxZMKodGfFUicNYds39CGqg/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**某地区多省份热力地图**
![](http://mmbiz.qpic.cn/mmbiz_png/x2S0icdguVdic6moA5Ek20duz2apg1GO3ibeomVdqblMia7rNUMy8PXdEuGkhZlDdjxh76lDSXmykJosNAnP3DGlMQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 如何使用该代码？

**只需一步：修改为自己的数据文件**. 

文件夹中找到对应省份或地区的数据文件，然后填入自己需要作图的数据然后保存即可。. 

## 该代码中主要可调整哪些参数？

轮廓线颜色:geom_polygon(colour="grey40")
填充的渐变色:scale_fill_gradient(low="white",high="steelblue")
指标引用:fill = zhibiao

## 注意事项
ggsave保存结果图片时，因为省份或城市标签是中文的，所以保存为pdf时会错误，应该保存成图片格式文件，如TIFF。
## Acknowledgement

谢谢大牛分享，本次学习掌握参考详细见[refer1](https://mp.weixin.qq.com/s?__biz=MzA3Njc0NzA0MA==&mid=2653188691&idx=1&sn=d85599f3599650a6d4bb6cb2ea4eea3c&scene=21#wechat_redirect), and [refer2](https://mp.weixin.qq.com/s?__biz=MzA3Njc0NzA0MA==&mid=2653188708&idx=1&sn=ecd1b61420444a5bb061a8b48c47c463&scene=21#wechat_redirect)and [refer3](https://mp.weixin.qq.com/s?__biz=MzA3Njc0NzA0MA==&mid=2653190213&idx=1&sn=4bbc3d46dae710fb5c276a3d82ce8ec6&chksm=848c400ab3fbc91cd8d1cad1aba440314dd58e033c993bb74cbbb7996fe9e129274dfcd69660&scene=21#wechat_redirect). 