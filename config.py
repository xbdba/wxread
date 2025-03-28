# config.py 自定义配置,包括阅读次数、推送token的填写
import os
import re

"""
可修改区域
默认使用本地值如果不存在从环境变量中获取值
"""

# 阅读次数 默认120次/60分钟
READ_NUM = int(os.getenv('READ_NUM') or 400)
# 需要推送时可选，可选pushplus、wxpusher、telegram
PUSH_METHOD = "" or os.getenv('PUSH_METHOD')
# pushplus推送时需填
PUSHPLUS_TOKEN = "" or os.getenv("PUSHPLUS_TOKEN")
# telegram推送时需填
TELEGRAM_BOT_TOKEN = "" or os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = "" or os.getenv("TELEGRAM_CHAT_ID")
# wxpusher推送时需填
WXPUSHER_SPT = "" or os.getenv("WXPUSHER_SPT")
# read接口的bash命令，本地部署时可对应替换headers、cookies
curl_str = os.getenv('WXREAD_CURL_BASH')

"""
建议保留区域|默认读三体，其它书籍自行测试时间是否增加
"""
data = {
    'appId': 'wb182564874663h776775553',
    'b': 'ce032b305a9bc1ce0b0dd2a',
    'c': '7cb321502467cbbc409e62d',
    'ci': 70,
    'co': 2968,
    'sm': '伪。还有学者提出一种"宇宙迫害妄想"学说',
    'pr': 75,
    'rt': 30,
    'ts': 1738739414820,
    'rn': 59,
    'sg': '9c4abe1628fc441bccf561ce907384a44e2eee228fd835d2634676978acd1e41',
    'ct': 1738739414,
    'ps': '9c4328507a5d1b12g012450',
    'pc': '09c326907a5d1b12g0138cd',
    's': '55451c61',
}

def convert(curl_command):
    """提取bash接口中的headers与cookies"""
    # 提取 headers
    headers_dict = {}
    for match in re.findall(r"-H '([^:]+): ([^']+)'", curl_command):
        headers_dict[match[0]] = match[1]

    # 提取 cookies
    cookies_dict = {}
    cookie_string = re.search(r"-b '([^']+)'", curl_command)
    if cookie_string:
        for cookie in cookie_string.group(1).split('; '):
            if '=' in cookie:
                key, value = cookie.split('=', 1)
                cookies_dict[key] = value

    return headers_dict, cookies_dict


headers, cookies = convert(curl_str) if curl_str else (headers, cookies)
