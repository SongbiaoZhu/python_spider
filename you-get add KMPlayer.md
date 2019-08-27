# you-get add KMPlayer

## 目的

实现通过you-get来免广告、免下载直接用本地播放器在线看视频。

## 步骤

* 下载KMPlayer，[网址](https://kmplayer.en.softonic.com)
* 安装KMPlayer，选择语言为英文，然后安装过程中均为默认选项，不做任何修改。
* 安装完成后，发现安装的路径为 C:\KMPlayer
* 添加KMPlayer到系统变量，windows徽标键--计算机--右键选择属性--高级系统设置--环境变量--系统变量中的Path鼠标左键选中--点击编辑...--先输入;作为分隔，然后粘贴C:\KMPlayer ，点击确定-确定即完成。注意一定不要修改Path路径中的其他内容。
* 测试 you-get -p KMPlayer "video url"
* 举例测试代码如下

```shell
you-get -p KMPlayer https://v.qq.com/x/cover/05wirht96yc89cg/e0911a13y5h.html
```

