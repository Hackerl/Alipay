#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading
import ConfigParser
import sys
import ConfigParser
import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

class alipay:
    def __init__(self):
        try:
            print '[+]读取cookie'
            config = ConfigParser.ConfigParser()
            config.read('Cookie.cfg')
            user = dict(config.items('alipay'))
            self.cookie= user['cookie']
            self.test_time = int(user['test_time'])
            self.get_time = int(user['get_time'])

        except:
            print '[-]读取cookie失败'

    def test_online(self):
        url = 'https://consumeprod.alipay.com/record/standard.htm'
        auth_header = {'Host':'consumeprod.alipay.com',
                    'Referer':'https://my.alipay.com/portal/i.htm',
                    'Cookie':self.cookie}
                    
        rsp = requests.get(url, headers=auth_header)
        if '登录' in rsp.text.encode('utf-8') and '注册' in rsp.text.encode('utf-8'):
            print '[-]cookie失效'
            #self.notice()  #发送邮件通知你cookie失效
            #sys.exit()     #停止运行
        else:
            print '[+]cookie有效'
            
    def keep_online(self):
        while(1):
            self.test_online()
            print '[+]保持登录结束 休息%d秒'%self.test_time   
            time.sleep(self.test_time)
            
    def notice(self):
        sender = '490021209@qq.com'
        receivers =['490021209@qq.com']   # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
    
        #创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = Header("Hackerl", 'utf-8')
        message['To'] =  Header("Hackerl", 'utf-8')
        subject = 'Cookie failed'
        message['Subject'] = Header(subject, 'utf-8')
    
        #邮件正文内容
        message.attach(MIMEText('Cookie failed', 'plain', 'utf-8'))
        
        try:
            smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)
            smtpObj.login('490021209@qq.com','秘钥 并非qq密码 需要申请')
            smtpObj.sendmail(sender, receivers, message.as_string())
            print "邮件发送成功"
        except smtplib.SMTPException:
            print '发送失败'

    def get_bill(self):
        print 'cookie:',self.cookie
        auth_header = {'Host':'consumeprod.alipay.com',
                    'Referer':'https://my.alipay.com/portal/i.htm',
                   'Cookie':self.cookie}
        rsp = requests.get('https://consumeprod.alipay.com/record/standard.htm', headers=auth_header)
        soup = BeautifulSoup(rsp.text,"html.parser")
        finish=[]
        f=open('zhifu.txt','a+')
        for w in f.readlines():
            try:
	        finish.append(w.split('|')[1][:-1])
	    except:
	        pass
        result=[]
        for q in soup.find_all("tr",class_="J-item"):
            mon_num = q.find_all("span",class_="amount-pay")[0].get_text().replace('\t','').replace(' ','').replace('\n','').replace('\r','').encode('utf-8')
            if mon_num == '+30.00' or mon_num == '+50.00':      #获取付款 30 或 50 的账单信息 可自行修改
                i=q.find_all("li",class_="btn-group-item",attrs={"data-target":"_blank"})[0]['data-link']
                if i in finish:
                    print 'finished:'+i
                else:
                    result.append(i)
        zhifu=[]
        
        if '登录' not in rsp.text.encode('utf-8'):
            print '[+]cookie work'
            for url in result:
                rsp_url = requests.get(url, headers=auth_header)
                soup_url = BeautifulSoup(rsp_url.text,"html.parser")
                user=''
                for i in soup_url.find_all("div",class_="tb-border p-trade-slips"):
                    user = i.find_all("td")[0].parent.get_text().replace('\t','').replace(' ','').replace('\n','').replace('\r','').encode('utf-8')
                #
                if '对方信息' in user:
                    user=user.split('对方信息：')[1]
                    mount=soup_url.find_all("td",class_="amount")[0].get_text().replace('\t','').replace(' ','').replace('\n','').replace('\r','').encode('utf-8')
                    if '留言' in user:
                        user=user.split('留言')[0]
                    if '=' in mount:
                        mount=mount[1:]
                    zhifu.append(user+'&'+mount+'|'+url.encode('utf-8')+'\n')
            f.writelines(zhifu)

        else:
            print '[-]cookie faild'
            
	    f.close()

    def get(self):
        while 1:
            self.get_bill()
            print '[+]获取账单结束 休息%d秒'%self.get_time   
            time.sleep(self.get_time)        

    def run(self):
        t1 = threading.Thread(target=self.get,args=())
        t2 = threading.Thread(target=self.keep_online,args=())
        t1.start()
        t2.start()
        
if __name__ =='__main__':
    alipay = alipay()
    alipay.run()
    
    
    
    
    
    
    
    
