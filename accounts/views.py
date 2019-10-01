from rest_framework import viewsets
from accounts.serializers import UserSerializer
from accounts.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.authtoken.models import Token


class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):

        for user in User.objects.all():
            token = Token.objects.get_or_create(user=user)
        return Response({"code": 0,
                             "msg": "login success!",
                             "token": token.key})


# TODO：用户退出登录，用户注册，用户密码重置，用户个人信息修改功能实现

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

