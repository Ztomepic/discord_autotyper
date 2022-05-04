import requests
import json
import time
import random


class AutoTyper():
    def __init__(self, authorization, channel_id, text, interval=86500, inner_interval=10):
        self.channel_id = channel_id
        self.authorization = authorization
        self.interval = interval
        self.inner_interval = inner_interval
        self.text = text

        self.count = 0

    def chat(self, auth, content):
        self.inner_sleep()
        # 伪装头
        header = {
            "Authorization": auth,
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        # 整理发送的内容、生成nonce
        msg = {
            "content": content,
            "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),  # 923802142370693120 923802484009336832
            "tts": False
        }
        # 拼接频道地址
        url = 'https://discord.com/api/v9/channels/{}/messages'.format(self.channel_id)
        res = requests.post(url=url, headers=header, data=json.dumps(msg))
        print(res.content)

    def inner_sleep(self, t1=10, t2=60):
        time.sleep(self.inner_interval + random.randint(t1, t2))

    def daily_sleep(self, t1=10, t2=60):
        print("daily sleep for {} seconds".format(self.interval))
        time.sleep(self.interval + random.randint(t1, t2))

    def batch_chat(self):
        print("task number:{}, time:{}".format(self.count, time.asctime(time.localtime(time.time()))))
        for auth_, text_ in zip(self.authorization, self.text):
            self.chat(auth_, text_)
        self.count += 1
        self.daily_sleep()


if __name__ == "__main__":
    channel_id = 123456789  # fill in channel id to which you want to send message
    text = ["""fill in what want to send 1""", """fill in what want to send 2"""]  # fill in what want to send. It's a list which contains text for every account
    authorization = ["autorization1", "autorization2"]  # fill authorization, find it in browser console. It's a list which contains authorization for every account
    autotyper = AutoTyper(authorization, channel_id, text)
    autotyper.batch_chat()
