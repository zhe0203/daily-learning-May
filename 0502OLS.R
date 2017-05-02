rm(list=ls())
setwd("C:/Users/jk/Desktop")
library(readxl)

# 读取数据
mydata = read_excel('指标转置.xlsx')
colnames(mydata)[1:10] = paste0('x',1:10)  # 重新命名数据的列
colnames(mydata)[11] = c('y')

# 建立回归方程
fm = y ~ x2+x3+x4+x5+x6+x7+x8+x9+x10
# 首先将全部的边距然如方程
fit = lm(fm,data=mydata)
summary(fit)

# 由于变量过多，采用逐步剔除的方法进行变量的选择
slm1 = step(fit)
summary(slm1)

fm1 = y~x2+x4+x5+x7+x8
summary(lm(fm1,data=mydata))

fit1 = lm(fm1,data=mydata)
#par(mfrow=c(2,2))
plot(fit1)
