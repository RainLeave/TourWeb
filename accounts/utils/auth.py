from rest_framework import exceptions
# from TourismShop import models
# from .models import TourToken
from accounts import models


class FirstAuthentication(object):
    """
    基类
    """

    def authenticate(self, request):
        pass

    # 下面方法不写会报错
    def authenticate_header(self, request):
        pass


class TourWebAuthentication(object):

    def authenticate(self, request):
        token = request._request.GET.get('token')
        # token表的对象
        # tokenobj = models.TourToken.objects.filter(token=token).first()
        tokenobj = models.TourToken.objects.filter(token=token).first()

        # 如果表为
        if not tokenobj:
            raise exceptions.AuthenticationFailed('用户认证失败')

        # 返回一个元组
        # 在rest framework 内部会将这两个字段赋值给request，以供后续操作使用
        return (tokenobj.user, tokenobj)

    # 弹出一个框
    def authenticate_header(self, request):
        pass
    #     # BasicAuthentication中的
    #     # BasicAuthentication基类方法响应头的作用
    #     # 认证就是基于浏览器来实现的
    #     # 用户登录认证，传过来的是个token，放在url中(token也可以放在请求头或者cookie中)
    #     # 比如路由器配置，配置地址后，会出现一个弹窗，要求输入用户名和密码（这个页面不是人写的，而是浏览器写的一个用户密码登录的程序，浏览器将用户名和密码放入请求头，加密后，发给服务器，解密后，再拿到用户名密码，加密解密这是个认证规则，叫做BasicAuthentication
    #     #
    #     # 认证就是基于浏览器实现的
    #     # 如果我们自己想要做这个认证，写上下面这句
    #     return 'Basic realm="api"'
    #
    #     # return 'Basic realm="%s"' % self.www_authenticate_realm

