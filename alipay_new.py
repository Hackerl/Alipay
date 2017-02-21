#!/usr/bin/env python
# -*- coding: utf-8 -*-
#可获取金额，订单号,时间

from bs4 import BeautifulSoup as bs
from requests.packages.urllib3 import connectionpool
import requests
import time
import logging
import sys
import ConfigParser

# EDIT START
class alipay:
    def __init__(self):
        try:
            print '[+]读取cookie'
            config = ConfigParser.ConfigParser()
            config.read('Cookie.cfg')
            user = dict(config.items('alipay'))
            self.cookie= {'ALIPAYJSESSIONID': user['cookie'].split('=')[1]}
        except:
            print '[-]读取cookie失败'


# EDIT END
    def bili(self,soup):
        PaymentID = []
        for i in soup.select('.consumeBizNo'):
            PaymentID.append(i.string.strip().encode('utf-8'))


        Time = []
        timeFormat = '%Y-%m-%d %H:%M:%S'
        for i in soup.select('.time'):
            Time.append(int(time.mktime(time.strptime(i.string.strip(), timeFormat))))


        Name = []
        for i in soup.select('.emoji-li'):
            for ii in i.stripped_strings:
                Name.append(ii.encode('utf-8'))


        Amount = []
        for i in soup.select('.amount.income'):
            Amount.append(i.string.encode('utf-8'))
        return PaymentID,Time,Name,Amount


    def run(self):
        req = requests.get('https://lab.alipay.com/consume/record/items.htm', cookies=self.cookie)
        if req.url.startswith('https://auth.alipay.com/'):
            print 'cookie失效'
            sys.exit(0)

        soup = bs(req.text, 'lxml')
        for i in soup.select('.amount.outlay'):
            i.parent.decompose()
        for i in soup.select('.subTransCodeValue'):
            i.decompose()

        PaymentID,Time,Name,Amount = self.bili(soup)
        length = len(PaymentID)

        f=open('zhifu.txt','a+')
        finish=[]
        for w in f.readlines():
            finish.append(w.split('|     ')[1][:-1])
        for i in range(length):
            if PaymentID[i] in finish:
                print 'finished:'+PaymentID[i]
            else:
                print (Name[i],Amount[i],Time[i],PaymentID[i])
                f.write('%s    &     %d    |     %s\n' % (Amount[i],Time[i],PaymentID[i]))
        time.sleep(5)
if __name__ =='__main__':
    alipay=alipay()
    alipay.run()
