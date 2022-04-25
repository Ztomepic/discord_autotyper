import requests, random
import json
import time


def chat(authorization, chanel_id, text):
    header = {
        "Authorization": authorization,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36"
    }
    # generate nonce
    msg = {
        "content": text,
        "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),  # 923802142370693120 923802484009336832
        "tts": False
    }
    # fill in chanel id
    url = 'https://discord.com/api/v9/channels/{}/messages'.format(chanel_id)
    res = requests.post(url=url, headers=header, data=json.dumps(msg))
    print(res.content)


if __name__ == "__main__":
    count = 0
    channel_id = 123456789  # fill in channel id to which you want to send message
    time_gap = 43260  # time gap, here is half a day
    text = """fill in what want to send"""  # fill in what want to send
    authorization = "authorization"  # fill in authorization, open discord in chrome, find it in console.
    while True:
        print("task number:{}, time:{}".format(count, time.asctime(time.localtime(time.time()))))
        chat(authorization, channel_id, text)
        count += 1
        time.sleep(time_gap)
