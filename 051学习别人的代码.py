# coding=utf-8
# http://mp.weixin.qq.com/s?__biz=MzAwNDc0MTUxMw==&mid=2649640019&idx=1&sn=dfebcd3c3d160eddb6a1cdc2d1bdb40a&chksm=833dacb5b44a25a3833e84771ef14e35c213e6a91f3b45c7811e0d7a9d1a5b2d4db65ee06d51&mpshare=1&scene=1&srcid=0325aFDW2dgLrkYS0HBNFOA2#rd

# 歌词的爬虫
import requests
import re
import urllib
from bs4 import BeautifulSoup
import codecs

def getPostdata(artistID=1158):
    s = requests.Session()
    postData = {'type':'artSong','artistID':artistID}
    return s,postData

def PrintLis(lis):
    for j in range(len(lis)):
        print(lis[j])

def Cleanit(Str):
    Str = Str.replace('</br>','')
    Str = Str.replace('<br/>','')
    Str = Str.replace('<div class="lrc" id="lrc_yes">','').strip()
    returnLis = Str.split('<br>')
    return returnLis

def WriteLis(fr,lis):
    for li in lis:
        fr.write(li + '\r\n')

def Crawl(s,headers,crawlist,crawlist_name):
    path_base = "D:\\Python Workspace\\Data\\LRC_许巍\\"
    geciurl_base = "http://www.kuwo.cn/geci/l_"
    for i in range(len(crawlist)):
        ID = crawlist[i]
        geciurl = geciurl_base + ID
        filename = str(i)
        path = path_base + filename + '.txt'
        print(crawlist_name[i],path,geciurl)
        fr = codecs.open(path,'w')
        req = s.get(geciurl,headers=headers)
        soup = BeautifulSoup(req.text,'html.parser')
        lrc_yes = soup.find_all(attrs = {'id':'lrc_yes'})
        if len(lrc_yes) == 0:
            continue
        returnLis = Cleanit(str(lrc_yes[0]))
        fr.write(crawlist_name[i],+'\r\n')
        WriteLis(fr,returnLis)
        fr.close()
        if i >= 103:
            break

def Get():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'http://passport.cnblogs.com/user/signin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
    }
    url = "http://www.kuwo.cn/geci/wb/getJsonData"
    s, postData = getPostdata()
    idtoname = {}
    Mylis = []
    for i in range(1, 23):
        postData['page'] = i
        req = s.post(url, data=postData, headers=headers)
        dic = req.content.decode()
        patids = re.compile('\"rid\":\"(.*)\"')
        patnames = re.compile('\"name\":\"(.*)\"')
        pat2 = re.compile('\[(.*)\]')
        js = pat2.findall(dic)[0]
        pat3 = re.compile('\{(.*?)\}')
        lis = pat3.findall(js)
        print(len(lis))
        for li in lis:
            sonlis = li.split(',')
            ids = patids.findall(sonlis[0])
            names = patnames.findall(sonlis[1])
            Mylis.append([ids[0], names[0].split(' ')[0].split('-')[0].split('(')[0]])
            # print(ids[0],names[0].split(' ')[0].split('-')[0])
            idtoname[ids[0]] = names[0]
    nameset = set([])
    crawlist = []
    crawlist_name = []
    for items in Mylis:
        # print(items)
        if items[1] not in nameset:
            nameset.add(items[1])
            crawlist.append(items[0])
            crawlist_name.append(items[1])
    Crawl(s, headers, crawlist, crawlist_name)


if __name__ == '__main__':
    Get()


import jieba
from operator import itemgetter
from math import log
def getpath(i):
    path = "D:\\Python Workspace\\Data\\LRC_许巍\\%d.txt" % i
    return path

def analysis():
    TF = {}
    IDF = {}
    Count = 0.0
    for i in range(103):
        filepath = getpath(i)
        nowdic = {}
        sumwords = 0.0
        try:
            with open(filepath) as fr:
                for line in fr.readlines():
                    line = line.stip()
                    lis = list(jieba.cut(line,cut_all=True))
                    sumwords += float(len(lis))
                    for li in lis:
                        if len(li) <= 1:
                            continue
                        if li not in IDF.keys():
                            IDF[li] = [i]
                        else:
                            IDF[li].append(i)
                        if li not in nowdic.keys():
                            nowdic[li] = 0.0
                        else:
                            nowdic[li] += 1.0
                Count += 1
                if sumwords > 0.0:
                    for key in nowdic.keys():
                        nowdic[key] = float(nowdic[key]/sumwords)
                        if key not in TF.keys():
                            TF[key] = nowdic[key]
                        else:
                            TF[key] += nowdic[key]
        except IOError as err:
            pass
    for key in IDF.keys():
        numdoc = float(len(set(IDF[key])))
        IDF[key] = log(Count/(numdoc+1.0))
    TF_IDF = TF
    for key in TF_IDF.keys():
        TF_IDF[key] = float(TF_IDF[key] * TF[key])
    print(len(TF))
    sortedDic = sorted(TF_IDF.items(), key=itemgetter(1), reverse=True)
    i = 0
    fw = open('D:\\Python Workspace\\Data\\许巍TFIDF.txt', 'w')
    for key in sortedDic():
        fw.write(str(key[0])+' '+str(key[1])+'\r\n')
        i += 1
        if i >= 40:
            continue
        print(key[0],key[1])
    fw.close()

if __name__ == '__main__':
    analysis()
