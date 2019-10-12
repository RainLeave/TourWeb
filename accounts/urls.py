from accounts.views import SmsCodeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'code', SmsCodeViewSet, base_name="code")
# https://blog.csdn.net/liujh_990807/article/details/86658647