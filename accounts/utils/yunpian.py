import json
import requests
from TourismShop.settings.base import APIKEY


class YunPian(object):
    """
    基于云片网实现短信验证码
    """

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"  # 取名为单条发送，方便以后拓展

    def send_sms(self, code, mobile):
        params = {
            "apikey": self.api_key,
            "mobile": mobile,
            # text的格式必须是模板格式（如果有），并对变量code进行替换
            "text": "【你的签名】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code)
        }

        response = requests.post(self.single_send_url, data=params)
        # 需要解析的response.text
        re_dict = json.loads(response.text)
        return re_dict


if __name__ == "__main__":
    # 用来测试发送功能，当DRF提供了相应的接口后，可以注释掉
    yun_pian = YunPian(APIKEY)
    # 因为是测试用，所以静态数据即可
    yun_pian.send_sms("你的验证码", "你的电话号码")


