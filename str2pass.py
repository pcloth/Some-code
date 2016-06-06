# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:27:45 2016
@author: pcloth
模块名称：
    随机叠加密钥加密字符串模块
优点介绍：
    相同字符串，相同密钥，每次加密结果随机（随机总数可以自己调节）
    
原理：
    拆分每一个字符的ord编码出来，用密钥数字进行加法运算，然后再chr回字符，由于密钥长
    度和顺序是较为随机
调用例子：
    加密字符串，后面一个参数是密钥，如果没有密钥(或者密钥低于12位字符)就采用默认24位
    密钥
    
特例：由于chr(1114111)最大值是1114111，所以设计这个最大值作为特殊标记，一旦用户的字
    符串ord值超过1110000，就添加特殊标记后用原始ord减去秘钥ord。
    
>>>encryption('中文加密测试','8sdf$^sdfaiui') 
'⻢乥旫勄尹涱谾'

>>>decryption('⻢乥旫勄尹涱谾','8sdf$^sdfaiui')
'中文加密测试'


"""


import random
   

#加密算法
def encryption(string,keys=''):
    if len(string)<=0:
        raise NameError('\n\n传入的字符串长度必须大于0\
        \nencryption(string,keys)    string length must >0 ')
    if len(keys)>12:
        key=[x for x in map(ord,keys)]
    else:
        key=[96,44,63,80,21,50,33,86,88,71,10,9,3,1,6,28,66,70,12,35,53,19,47,93] #密钥序列，随机步长取这个序列
    maxi=len(key) 
    ret_txt=''
    key_i=0
    setp=random.randint(1,5) #随机密钥步长
    for r in string:
        if ord(r)>=1110000: #一旦发现超大值的字符，添加一个最大值的特殊字符
            ret_txt+=chr(1114111)
            ret_txt+=chr(ord(r)-key[key_i])
        else:
            ret_txt+=chr(ord(r)+key[key_i])
        key_i+=setp
        if key_i>=maxi:
            key_i=key_i-maxi
    return chr(1110000+setp)+ret_txt

#解密算法
def decryption(string,keys=''):
    if len(string)<=0:
        raise NameError('\n\n传入的字符串长度必须大于0\
        \ndecryption(string,keys)    string length must >0 ')
    if len(keys)>12:
        key=[x for x in map(ord,keys)]
    else:
        key=[96,44,63,80,21,50,33,86,88,71,10,9,3,1,6,28,66,70,12,35,53,19,47,93]
    maxi=len(key) 
    ret_txt=''
    key_i=0
    change_minus=0 #改减法标记
    if ord(string[0])<1110001:
        raise NameError('\n\ndecryption函数输入参数必须是经过encryption加密的字符串。\
        \nDecrypt function parameters must be encrypted')
    setp=ord(string[0])-1110000
    for r in string[1:]:
        if ord(r)==1114111:
            change_minus=1
            continue
        elif change_minus==1:
            ret_txt+=chr(ord(r)+key[key_i])
            change_minus=0
        else:
            ret_txt+=chr(ord(r)-key[key_i])
        key_i+=setp
        if key_i>=maxi:
            key_i=key_i-maxi
    return ret_txt
    

