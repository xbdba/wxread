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
