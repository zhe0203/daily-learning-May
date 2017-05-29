# 设置工作目录
setwd("C:/Users/jk/Desktop/Apriori")
# 加载Apriori算法包
library(arules)    # 未安装，需安装 install.packages('arules')

# 第一步：数据的读取与处理
## 读取数据
df = read.csv('数据.csv')
## df数据无法使用arules进行识别，因此需要进行如下转换
mydata = sapply(1:37,function(x) paste(colnames(df)[which(df[x,]==1)],collapse = ';'))
mydata=as.data.frame(mydata)
write.csv(mydata,'new_df.csv')

# 第二步：建立关联规则模型
## 读取新处理好的数据
apr_data = read.transactions("new_df.csv", sep = ';')
# 查看par_data数据的列名称，以确保正确进行稀疏矩阵的转换
colnames(apr_data)    # 转换成功
summary(apr_data)    # 查看数据概况
dim(apr_data)        # 查看数据维度

my_rules <- apriori(apr_data, parameter = list(support = 0.2, 
                                         confidence = 0.7,minlen = 2,maxlen=4))
my_rules_df <- as(my_rules, "data.frame")

# 第三步：将数据进一步整理
library(tidyr)    # 未安装，需安装 install.packages('tidyr')
#　将my_rulse_df结果中的rules分为lhs和rhs以便更好的查看数据
result = separate(my_rules_df,rules, c("lhs", "rhs"),sep='=>')
# 将result结果中的{}去掉
result['lhs'] = sapply(result['lhs'],function(x) sub('\\{(.+)\\}','\\1',x))
result['rhs'] = sapply(result['rhs'],function(x) sub('\\{(.+)\\}','\\1',x))
write.csv(result,'result.csv')   # 将结果输出
