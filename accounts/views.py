from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.db import models
from .models import Account

import http.client,urllib,hashlib,datetime,time,json,ssl;  #加载模块
import random
from django.http import JsonResponse

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

# 判断是否存在，如果不存在，则为注册，保存用户手机号并验证验证码是否正确；如果存在则为登录，直接验证验证码是否正确。
def login(request):
    user = get_object_or_404(Article, pk=article_id)

#定义账号和密码，开户之后可以从用户中心得到这两个值
accountSid = '7fe7310e3d42a1d2116b12dd6aef656f'
acctKey = 'ef7a74533e6cc0d9827d7ce7de6d1cbe'

#定义地址，端口等
serverHost = "openapi.miaodiyun.com"
serverPort = 443
industryUrl = "/distributor/sendSMS"

#发送行业短信
def send_message(request):
    mobile = request.GET.get('mobile')

    # 定义一个字符串,存储生成的6位数验证码
    message_code = ''
    for i in range(6):
        i = random.randint(0, 9)
        message_code += str(i)
    # 拼接成发出的短信

    text = "【币市头条】您的验证码为"+ message_code +"，该验证码5分钟内有效。请勿泄漏于他人。"

    #格式化时间戳，并计算签名
    timeStamp = str(int(round(time.time() * 1000)))
    rawsig = accountSid + acctKey + timeStamp
    m = hashlib.md5()
    m.update(rawsig.encode('utf-8'))
    sig = m.hexdigest()

    #定义需要进行发送的数据表单
    params = urllib.parse.urlencode({'accountSid':accountSid,
    'smsContent':text,
    'to':mobile,
    'timestamp':timeStamp,
    'sig':sig})

    #定义header
    headers = {"Content-Type":"application/x-www-form-urlencoded", "Accept":"application/json"}

    #与构建https连接
    conn = http.client.HTTPSConnection(serverHost, serverPort)

    #Post数据
    conn.request(method = "POST", url = industryUrl, body = params, headers = headers)

    #返回处理后的数据
    response = conn.getresponse()
    #读取返回数据
    jsondata = response.read()

    #打印完整的返回数据
    print(jsondata.decode('utf-8'))

    return JsonResponse(eval(jsondata.decode('utf-8')))

    #解析json，获取特定的几个字段
    jsonObj = json.loads(jsondata);
    respCode = jsonObj['respCode'];


    #关闭连接
    conn.close()
