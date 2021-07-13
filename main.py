import requests
import time
import random


def generate_random_str(randomlength):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str


def Code_1():
    print('（1）开始访问获取客户订阅日期详细信息：GetCustSubscribeDateDetail')
    time.sleep(int_time)
    payload = {
        'act': 'GetCustSubscribeDateDetail',
        'pid': p_id,
        'id': '243',
        'scdate': yuyue_times,
    }
    code = requests.get(
        url="https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx",
        headers=headers, cookies=cookie, params=payload, verify=False)
    # 转json
    if int(code.status_code) == 200:
        code_json_dict = code.json()
        print(code_json_dict)
        if int(code_json_dict['status']) == 200:
            print(code_json_dict['list'][0]['mxid'])
            mxid = code_json_dict['list'][0]['mxid']
            check_mxid = False
            return check_mxid, mxid
        else:
            check_mxid = True
            mxid = ''
            return check_mxid, mxid
    else:
        print(code.status_code)
        check_mxid = True
        print('访问异常,继续访问')
        mxid = ''
        return check_mxid, mxid


def Code_2():
    # 获取验证码
    print('（2）访问验证码：GetCaptcha')
    time.sleep(int_time)
    payload = {
        'act': 'GetCaptcha',
    }
    code = requests.get(
        url="https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx",
        headers=headers, cookies=cookie, params=payload, verify=False)
    # 转json
    if int(code.status_code) == 200:
        ck_s = YanZheng302()
        return ck_s
    else:
        print('访问异常,继续访问%s' % code.status_code)
        ck_s = True
        return ck_s


def GetCustSubscribeDateDetail():
    print('访问获取客户订阅日期详细信息：GetCustSubscribeDateDetail')
    time.sleep(int_time)
    payload = {
        'act': 'GetCustSubscribeDateDetail',
        'pid': p_id,
        'id': '243',
        'scdate': yuyue_times,
    }
    code = requests.get(
        url="https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx",
        headers=headers, cookies=cookie, params=payload, verify=False)
    # 转json
    if int(code.status_code) == 200:
        code_json_dict = code.json()
        print(code_json_dict)
        if int(code_json_dict['status']) == 200:
            print(code_json_dict['list'][0]['mxid'])
            mxid = code_json_dict['list'][0]['mxid']
            check_mxid = False
            return check_mxid, mxid
        else:
            check_mxid = True
            mxid = ''
            return check_mxid, mxid
    else:
        print(code.status_code)
        check_mxid = True
        print('访问异常,继续访问')
        mxid = ''
        return check_mxid, mxid


def YanZheng302():
    print("（3）开始验证：CaptchaVerify")
    time.sleep(int_time)
    payload = {
        'act': 'CaptchaVerify',
        'token': '',
        'x': x,
        'y': '5',
    }
    code = requests.get(
        url="https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx",
        headers=headers, cookies=cookie, params=payload, verify=False)
    # 转json
    if int(code.status_code) == 200:
        code_json_dict = code.json()
        print(code_json_dict)
        if int(code_json_dict['status']) != 204 and int(code_json_dict['status']) != 201:
            if int(code_json_dict['status']) != 408:
                print('验证码-验证成功')
                print('guid:%s' % code_json_dict['guid'])
                guid = code_json_dict['guid']
                Checks = False
                # 成功后去访问Save20结果去提交数据=预约成功
                print('（4）马上提交')
                Save20(yuyue_times, p_id, mxid, guid)
                return Checks
            else:
                Checks = True
                print('请重新授权Cookies')
                return Checks
        else:
            Checks = True
            print('继续验证')
            return Checks


def Save20(times, p_id, mxid, guid):
    payload = {
        'act': 'Save20',
        'birthday': "1999-02-22",
        'tel': "15521779388",
        'sex': "2",
        'cname': "王培",
        'doctype': "1",
        'idcard': "440223199902282747",
        'mxid': mxid,
        'date': times,
        'pid': p_id,
        'Ftime': "1",
        'guid': guid,
    }
    print(payload)
    tongyong = requests.get(
        url="https://cloud.cn2030.com/sc/wx/HandlerSubscribe.ashx",
        headers=headers, cookies=cookie, params=payload, verify=False)
    # 转json
    json_dict = tongyong.json()
    print(json_dict)
    if int(json_dict['status']) != 201:
        print(json_dict)
        print('预约成功')
    else:
        pass


if __name__ == '__main__':
    # 延迟时间
    int_time = 4
    # Cookies
    cookies = 'd23gu3r1q2qznhf5xra5en05'
    cookie = {
        "ASP.NET_SessionId": cookies
    }
    headers = {
        'charset': 'utf-8',
        'Accept-Encoding': 'gzip',
        'referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/73/page-frame.html',
        'cookie': '',
        'content-type': 'application/json;text/plain;*/*',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Redmi Note 7 Build/PKQ1.180904.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36 MicroMessenger/7.0.6.1460(0x27000634) Process/appbrand0 NetType/4G Language/zh_CN',
        # 'Host': 'blog.csdn.net',
        'Host': 'cloud.cn2030.com',
        'Connection': 'Keep-Alive'
    }
    requests.packages.urllib3.disable_warnings()
    # 猜测验证码的X
    x = '33'
    Checks = True
    # 测试
    yuyue_times = '2021-05-24'
    # 1= 九价
    p_id = '12'
    # 获取订阅日期mxid
    while Checks:
        Checks, mxid = Code_1()

    # 获取验证码
    Checks2 = True
    while Checks2:
        Checks2 = Code_2()

    # 7Q90AC5oAABeYzQB = 26670
