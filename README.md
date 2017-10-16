# Alipay
支付宝交易信息爬虫
推荐使用alipay_new，alipay代码较乱，懒得重构

# 用法

配置Cookie.cgf

    [alipay]
    cookie = ALIPAYJSESSIONID=RZ05jON66r5SUgJJcklt1kXxDimrohauthRZ1
    test_time = 60              #定时访问支付宝 保持cookie有效性 建议60s
    get_time = 60               #定时获取账单信息

关于Cookie需要登录支付宝后按下F12，然后再console上面输入document.cookie，或者到开发者工具中查看HTTP报文

Cookie 只需要其中一个字段:

    ALIPAYJSESSIONID=xxxxxxxxxxxxx


# 说明
alipay 可获取对方名字，手机或邮箱，金额，订单号网址，集成了qq邮件模块，可以直接调用，发送邮件:

    sender = '490021209@qq.com'
    receivers =['490021209@qq.com']   # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

qq邮件秘钥需要申请，请自行搜索

alipay_new 可获取金额，订单号,时间，使用另外的api，没有写保持cookie模块，可自行添加

结果:

    姓名187****3962&30.00|https://shenghuo.alipay.com/send/queryTransferDetail.htm?tradeNo=20170221200040011100460045967033
    用户名  手机号    金额                    订单号信息
    
    30.00    &     1487677389    |     20170221200040011100790046934184
    金额             时间                     订单号
