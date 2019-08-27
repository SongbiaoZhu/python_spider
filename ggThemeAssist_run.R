rm(list = ls())
options(stringsAsFactors = F)
# install.packages("ggThemeAssist")
library(ggplot2)
library(ggThemeAssist)
# 使用mtcars生成一个点图示例
gg <- ggplot(mtcars, aes(x = hp, y = mpg, colour = as.factor(cyl))) + geom_point()
# 开始调整主题
#ggThemeAssistGadget(gg)
gg <- gg + theme(plot.subtitle = element_text(vjust = 1), 
    plot.caption = element_text(vjust = 1), 
    axis.line = element_line(size = 0.5, 
        linetype = "solid"), axis.title = element_text(face = "bold"), 
    axis.text = element_text(family = "sans", 
        size = 11, face = "bold"), legend.text = element_text(size = 11, 
        face = "bold"), legend.title = element_text(size = 11, 
        face = "bold"), panel.background = element_rect(fill = NA, 
        size = 0.8), plot.background = element_rect(colour = NA), 
    legend.key = element_rect(fill = "white"), 
    legend.background = element_rect(fill = NA))
ggsave('test.jpeg')
