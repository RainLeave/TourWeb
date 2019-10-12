from django.apps import AppConfig


class AccountsConfig(AppConfig):
    name = 'accounts'


def ready(self):
    """
    信号量实现密码加密
    重载函数ready
    实际上重载create方法更加灵活，而signal机制使得代码分离性更优。我们实际上可以自定义一些signal，不过我们要自己掌握发出信号的时机。
    """
    import accounts.signals