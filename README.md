#Alipay
支付宝交易信息爬虫

# 用法

配置Cookie.cgf

    [alipay]
    cookie = ALIPAYJSESSIONID=RZ05jON66r5SUgJJcklt1kXxDimrohauthRZ1
    test_time = 60              #定时访问支付宝 保持cookie有效性 建议60s
    get_time = 60               #定时获取账单信息

关于Cookie需要登录支付宝后按下F12，然后再console上面输入document.cookie复制cookie。
只需要：

    ALIPAYJSESSIONID=xxxxxxxxxxxxx


# 说明
集成了qq邮件模块，可以直接调用，发送邮件
qq邮件秘钥需要申请，请自行搜索

结果:

    姓名187****3962&30.00|https://shenghuo.alipay.com/send/queryTransferDetail.htm?tradeNo=20170221200040011100460045967033
    用户名  手机号    金额  订单号信息
