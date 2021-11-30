import requests

import time
import json
import base64


class Vpn:
    def __init__(self, params):
        self.url = 'http://192.168.254.17/drcom/login'#请求URL
        self.user = params.get('user')
        self.pwd = params.get('pwd')
        self.type = params.get('type')
        self.type_list = ['', '@cmcc', '@unicom', '@telecom']

    def login(self):
        get_params = {#实测保留四个关键参数是可以正常登录校园网络的
            'callback': 'dr' + str(int(time.time() * 1000)),
            'DDDDD': self.user + self.type_list[self.type],
            'upass': self.pwd,
            '_': str(int(time.time() * 1000)),
        }
        r = requests.get(self.url, params=get_params).text
        r = r.split('(')[1].split(')')[0]#将dr的括号解除。
        print(r)
        r = json.loads(r)
        print(r)

        # 建议测试登陆成功后，将下述代码注释
        ####################
        if r['result'] == 1:
            print('登陆成功')
        else:
            msg = r.get('msg')
            if msg == 'userid error1':
                print('不存在此用户，请检查用户名是否填写错误，或者运行商选择错误')
            elif msg == 'userid error2':
                print('用户密码错误')
            elif msg:
                print('未知错误：', msg)
            else:
                print('无错误：', msg)
        ####################


if __name__ == '__main__':
    user_info = {
        'user': '｛账号｝',  # JSUID
        'pwd': '｛密码｝',  # JSUID密码
        'type': 3,  # 0,1,2,3分别对应校园网、移动、联通与电信。
    }
    vpn = Vpn(user_info)
    while True:
        vpn.login(user_info)
        time.sleep(3600)#原代码5s检测一次登录情况，我给改成1h了
