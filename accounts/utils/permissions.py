from accounts.models import User


class MyPermission(object):
    # 继承并实现原生的权限类中的方法

    def has_permission(self, request, view):
        pass
        # 用户注册可以访问
        # print(request.user)
        #
        # # if request.user.GENDER == '女':
        # # 如果当前用户已经登录 才有权限
        # # Django2.0: HttpRequest.user属性
        # # if request.user:
        #     return False
        # # 返回True表示有权访问
        # return True


class MyPermission1(object):
    # 继承并实现原生的权限类中的方法

    def has_permission(self, request, view):
        # 用户注册可以访问
        print(request.user)
        if request.user.nickname:
            return False
        # 返回True表示有权访问
        return True


