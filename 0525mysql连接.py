# -*- coding=utf-8 -*-
 
 

 
import os
import MySQLdb
import logging
 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

 

logging.basicConfig(filename=log_file, level=logging.DEBUG)
 
# 把语句中所有的分词都写入到一个文件all_tags.txt，可以形成词云
#感兴趣的词计入interesting_tags.txt
# 然后可以针对interesting_tags中的词在每一篇文章中出现的权重（或者仅仅考虑出现次数）以及已经打的类别，从而可以自动判断出新文章的类别


def main():

    #传入用户名和密码
    dbuser ="zhangliang"
    dbpass ="Zl2017@2017"
    dbhost="120.26.95.149"
    dbname="yearly"
 

    arr_tags = []
    # html_tags 需要从文件中读取，因为可能很大,一行一个，一行中多个,以|隔开会被认为是同一个tag的同义词
  

    db = MySQLdb.connect( dbhost, dbuser ,dbpass,dbname,charset="UTF8")
    cursor = db.cursor()
    # SQL 那些记录需要取出来
   
    sql = "select id, content from cx0308 limit 10";
	


    print sql

    #jieba.load_userdict('guoshou.txt')
    #jieba.analyse.set_stop_words("stop_words.txt")
    #取出训练集合
    # data

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()

        for row in results:
            id = row[0]
          
            content = row[1]
           
            #print tmp_row
            print id, content

         

    except Exception as e:
        print "Error: unable to fecth data"
        print e

    # 关闭数据库连接
    db.close()
    print "done"
    csvfile.close()


if __name__ == "__main__":
     main()
     #下面是测试
     #print get_tags('基金3号产品和基金21号')
