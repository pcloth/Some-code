# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:27:45 2016
@author: pcloth
模块名称：
    随机叠加密钥加密字符串模块
优点介绍：
    相同字符串，相同密钥，每次加密结果随机（随机总数可以自己调节）
    
原理：
    拆分每一个字符的ord编码出来，用密钥数字进行加法运算，然后再chr回字符，由于密钥长度和
    顺序是较为随机
调用例子：
#加密字符串，后面一个参数是密钥，如果没有密钥(或者密钥低于12位字符)就采用默认24位密钥
>>>encryption('中文加密测试','8sdf$^sdfaiui') 
'⻢乥旫勄尹涱谾'
>>>decryption('⻢乥旫勄尹涱谾','8sdf$^sdfaiui')
'中文加密测试'
"""


import random
   

#加密算法
def encryption(string,keys=''):
    if len(keys)>12:
        key=[x for x in map(ord,keys)]
    else:
        key=[96,44,63,80,21,50,33,86,88,71,10,9,3,1,6,28,66,70,12,35,53,19,47,93] #密钥序列，随机步长取这个序列
    maxi=len(key) 
    ret_txt=''
    key_i=0
    setp=random.randint(1,5) #随机密钥步长
    for r in string:
        if ord(r)>=1110000:
            ret_txt+=chr(ord(r)-key[key_i])
        else:
            ret_txt+=chr(ord(r)+key[key_i])
        key_i+=setp
        if key_i>=maxi:
            key_i=key_i-maxi
    return chr(12000+setp)+ret_txt

#解密算法
def decryption(string,keys=''):
    if len(keys)>12:
        key=[x for x in map(ord,keys)]
    else:
        key=[96,44,63,80,21,50,33,86,88,71,10,9,3,1,6,28,66,70,12,35,53,19,47,93]
    maxi=len(key) 
    ret_txt=''
    key_i=0
    setp=ord(string[0])-12000
    for r in string[1:]:
        if ord(r)>=1110000:
            ret_txt+=chr(ord(r)+key[key_i])
        else:
            ret_txt+=chr(ord(r)-key[key_i])
        key_i+=setp
        if key_i>=maxi:
            key_i=key_i-maxi
    return ret_txt
    

