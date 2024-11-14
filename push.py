import requests
from datetime import datetime

# 企业微信相关配置
AGENT_ID = '1000004'
SECRET = 'kCLigbv6qylgAmEQXfYlouTYPa3irZvBzgn3Tm7apE0'
CORP_ID = 'ww02a13f5386a05f87'
ACCESS_TOKEN_URL = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
SEND_MSG_URL = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'

def get_access_token(corp_id, secret):
    """获取企业微信的access token"""
    url = f"{ACCESS_TOKEN_URL}?corpid={corp_id}&corpsecret={secret}"
    response = requests.get(url)
    data = response.json()
    
    if 'access_token' in data:
        return data['access_token']
    else:
        raise Exception("获取access token失败: {}".format(data))

def push(content):
    """发送企业微信消息，默认发给所有用户"""
    try:
        # 获取当前日期，格式化为 YYYY-MM-DD
        current_date = datetime.now().strftime('%Y-%m-%d')
        
        # 获取access token
        access_token = get_access_token(CORP_ID, SECRET)
        
        # 消息内容
        msg_data = {
            "touser": "@all",  # 发送给所有用户
            "msgtype": "text",
            "agentid": AGENT_ID,
            "text": {
                "content": f"{current_date}\n\n{content}"
            },
            "safe": 0
        }
        
        # 发送消息
        response = requests.post(SEND_MSG_URL.format(access_token), json=msg_data)
        result = response.json()
        
        if result.get('errcode') == 0:
            print("消息发送成功")
        else:
            print("消息发送失败: {}".format(result))
    
    except Exception as e:
        print("发生异常: {}".format(e))
