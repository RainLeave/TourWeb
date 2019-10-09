from accounts.models import User


class MyPermission(object):
    # 继承并实现原生的权限类中的方法

    def has_permission(self, request, view):
        # 用户注册可以访问
        # print(request.user)

        if request.user.GENDER == '男':
            return False
        # 返回True表示有权访问
        return True


class MyPermission1(object):
    # 继承并实现原生的权限类中的方法

    def has_permission(self, request, view):
        # 用户注册可以访问
        print(request.user)
        if request.user.nickname:
            return False
        # 返回True表示有权访问
        return True


