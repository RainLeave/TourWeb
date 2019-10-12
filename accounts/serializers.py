from accounts.models import User
from rest_framework import serializers

# yunpian sms
import re
from datetime import datetime
from datetime import  timedelta
from TourismShop.settings.base import REGEX_MOBILE


from accounts.models import SmsCode

class SmsSerializer(serializers.Serializer):
    """
    sms:短信
    验证码以短信的形式发送
    这里不继承ModelSerializer
    因为在model设计时，code是必填字段
    如果继承了ModelSerializer， 就会将表单和VerifyCode做一个关联
    则在点击发送验证码时，会报验证码必填的错
    所以继承Serializer自己写逻辑进行保存
    """

    # 有了这个声明，下面就可以对这个mobile进行校验
    mobile =  serializers.CharField(max_length=11)

    def validate(self, mobile):
        """
        验证手机号码
        """
        # 1、验证手机是否注册
        if User.object.filter(mobile=mobile).count():
            raise serializers.ValidationError('用户已经存在')

        # 2、验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 3、验证码发送频率
        # 当前时间-xxx = 一分钟前的时间
        one_minutes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if SmsCode.objects.filter(add_time__gt=one_minutes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'nickname']



