import requests
import json
import time


class DamaiTicketBot:
    def __init__(self, event_id, user_agent):
        self.event_id = event_id
        self.user_agent = user_agent

        self.headers = {
            'User-Agent': user_agent
        }

    def login(self, username, password):
        login_url = 'https://passport.damai.cn/login?ru=https%3A%2F%2Fwww.damai.cn%2F'

        payload = {
            'username': username,
            'password': password,
            'source': 'react',
            'remember': '0'
        }

        response = requests.post(login_url, headers=self.headers, data=payload)
        response_data = response.json()

        if response_data['status'] != 0:
            raise Exception('登录失败')

        self.access_token = response_data['data']['accessToken']

    def get_ticket_status(self):
        status_url = f'https://search.damai.cn/external/gl.html?keyword={self.event_id}'

        response = requests.get(status_url, headers=self.headers)
        response_data = json.loads(response.text.split('=')[1].split(';')[0])

        if response_data['errno'] != 0:
            raise Exception('获取票务状态失败')

        return response_data['data'][0]['status']

    def buy_ticket(self):
        buy_url = 'https://piao.damai.cn/quickbuygetprod'

        payload = {
            'itemId': self.event_id,
            'buyNum': '1',
            'channel': 'damai',
            'source': 'react',
            'access_token': self.access_token
        }

        response = requests.get(buy_url, headers=self.headers, params=payload)
        response_data = response.json()

        if response_data['status'] != 200:
            raise Exception('抢票失败')

        return response_data['data']

    def run(self, username, password):
        self.login(username, password)

        while True:
            ticket_status = self.get_ticket_status()

            if ticket_status == '立即购买':
                try:
                    ticket_info = self.buy_ticket()
                    print('抢票成功！票务信息：', ticket_info)
                    break
                except:
                    print('抢票失败，稍后重试')
            else:
                print('票务状态不可购买，正在重试...')

            time.sleep(1)


if __name__ == '__main__':
    event_id = '668400238286'  # 活动ID
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'  # 自定义User-Agent

    bot = DamaiTicketBot(event_id, user_agent)
    bot.run('18054563442', 'Zty2023Damai')