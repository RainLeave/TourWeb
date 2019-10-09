from rest_framework import viewsets
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework.authtoken.models import Token
from accounts.models import User, TourToken
from rest_framework.generics import GenericAPIView
from rest_framework import status
#
# class UserLoginViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def post(self, request, *args, **kwargs):
#
#         for user in User.objects.all():
#             token = Token.objects.get_or_create(user=user)
#         return Response({"code": 0,
#                              "msg": "login success!",
#                              "token": token.key})

def md5(user):
    """
    生成随机字符串
    :param user:
    :return:
    """
    import hashlib
    import time

    ctime = str(time.time())

    # str convert byte
    m = hashlib.md5(bytes(user, encoding="utf-8"))
    m.update(bytes(ctime, encoding="utf-8"))
    return m.hexdigest()


class UserLoginView(APIView):

    # 当在配置文件中全局配置了认证类的时候，存在局部视图如如AuthView登录的视图，就不需要做认证
    # 因为token是用户登录才生成的，用户还未登录，不需要做认证
    # 这个时候可以设置authentication_classes=空列表
    # 执行的时候会先看当前类是否存在认证类，当前类不存在往父类中找

    authentication_classes = [ ]

    # 输入用户名和密码用POST请求，涉及到检测用户名和密码
    def post(self, request, *args, **kwargs):

        ret = {'code': 1000, 'msg': None}

        # 获取表单中输入的用户名和密码
        # request已经不再是原来的request,如果想要用原来的request做，使用._request
        # 用户通过手机号和用户昵称进行注册
        nickname = request._request.POST.get('nickname')
        mobile = request._request.POST.get('mobile')

        obj = User.objects.filter(mobile=mobile, nickname=nickname)

        if not obj:
            ret['code'] = 1001
            ret['msg'] = "用户名或密码错误"

        # 为登录用户通过MD5来创建token
        token = md5(nickname)
        # 存在就更新，不存在就创建
        TourToken.objects.update_or_create(user=obj, default={'token': token})







from django.http import  HttpResponse
from accounts.utils.permissions import MyPermission
from accounts.utils.auth import TourWebAuthentication


class UserInfoView(APIView):
    """
    用户信息
    只有登录用户才有权限查看
    """
    # 在设置文件中全局配置权限
    authentication_classes = [TourWebAuthentication, ]
    permission_classes = [MyPermission, ]

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return HttpResponse("用户信息")


# TODO：用户退出登录，用户注册，用户密码重置，用户个人信息修改功能实现
class UserLogoutView(GenericAPIView):
    """
    用户退出登录
    存在检测用户数据？因为是post方法
    """
    authentication_classes = [TourWebAuthentication, ]
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [MyPermission, ]

    def post(self, request):
        TourToken.objects.filter(user=request.user).updat(expires=datetime.datetime.now())
        return Response(status=status.HTTP_200_OK)




# 商品模块功能的实现：商品列表，商品类别，购物车功能
# 支付模块实现

# 后续的以后再说
# 第三方功能
# uwsgi+nginx部署
# 代码日志测试,logger

#
# curl -X POST -H "Content-Type: application/json"   -d '{"username": "12", "password": "Lijunjun123"}'   http://127.0.0.1:8000/api-token-auth/


"""
订单业务限制登录的人才可以看
1、判断登录的用户
2、如何实现

class OrderViewSet(GenericAPIView):
    serializer_class = UserSerializer
    authentication_classes = (TourWebAuthenticate,)
    permission_classes = (IsAuthenticated,)
    
    # 视图函数的第一个参数必须是request
    def post(self, request, *args, **kwargs):
        self.dispatch
        """
        # User Login with email or phone
        # :param request:
        # :return:
        # """
        # token = request._request.GET.get('token')
        # if not token:
        #     return HttpResponse("用户未登录")
        # ret = {'code': 10000,  'msg': None, 'data': None}
        #
        # # 用try包裹，保证代码的正确性
        # try:
        #
        #     ret['data'] = ORDER_DICT
        # except Exception as e:
        #     pass
        #
        # return JsonResponse(ret)

