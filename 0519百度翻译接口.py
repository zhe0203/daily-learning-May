# -*- coding: utf-8 -*-
import httplib
import md5
import urllib
import random

# 请先将需要翻译的文本转换为UTF-8编码
'''
语言列表：源语言语种不确定时可设置为auto,目标语言语种不可设置为auto
    auto 自动检测 zh 中文 en 英文 yue 粤语 wyw 文言文 jp 日语
    kor 韩语 fra 法语 spa 西班牙语 th 泰语 ara 阿拉伯语
    ru 俄语 pt 葡萄牙语 ..........更多查看文档
    http://api.fanyi.baidu.com/api/trans/product/apidoc
'''
'''
from 翻译源语言
to 译文语言
trans_result 翻译结果
src 原文
dst 译文
'''


appid = '20170519000048502'
secretKey = 'qxu2IRx_3JKIaaJWrq91'

httpClient = None
myurl = '/api/trans/vip/translate'
q = 'apple'
fromLang = 'en'
toLang = 'zh'
salt = random.randint(32768,65536)

sign = appid + q + str(salt) + secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appid='+appid+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign

try:
    httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET',myurl)

    # response是HTTPResonse对象
    response = httpClient.getresponse()
    print(response.read())

except Exception as e :
    print(e)

finally:
    if httpClient:
        httpClient.colse()
