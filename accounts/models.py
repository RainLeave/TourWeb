from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings
from datetime import timedelta, datetime


class Country(models.Model):
    # COUNTRY_CODE = (
    #     (1, 'China'),
    #     ('2', 'English'),
    #     ('3', 'Singapore')
    # )
    country_name = models.CharField(max_length=30, null=True, blank=True, verbose_name=u"国家")
    description = models.CharField(
        _("description"),
        max_length=2048,
        null=False,
        blank=False,
    )

    class Meta:
        app_label = "accounts"  # 这里，指明app名称，用来对应app 和 数据库的map表
        db_table = "Country"


class Region(models.Model):
    S, H, N = range(3)
    REGION_CODE = (
        (S, u'上海'),
        (H, u'杭州'),
        (N, u'南京')

    )
    region_code = models.CharField(choices=REGION_CODE, max_length=30,
                                   null=True, blank=True, verbose_name=u"地区代码")
    country_code = models.ForeignKey(Country, max_length=30, on_delete=models.PROTECT,
                                     null=True, blank=True, verbose_name=u"地区代码")
    description = models.CharField(
        _("description"),
        max_length=2048,
        null=False,
        blank=False,
    )


class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(email=email,
                          first_name=first_name,
                          last_name=last_name,
                          is_active=True,
                          last_login=now,
                          date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, first_name, last_name, password, **extra_fields):
        """
        Create and save an User with the given email, password and name.

        :param email: string
        :param first_name: string
        :param last_name: string
        :param password: string
        :param extra_fields:
        :return: User
        """

        return self._create_user(email, password, first_name, last_name, is_staff=False, is_superuser=False,
                                 **extra_fields)

    def create_superuser(self, email, first_name='', last_name='', password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        return self._create_user(email, password, first_name, last_name, is_staff=True, is_superuser=True,
                                 **extra_fields)


class User(AbstractUser):
    """
    自定义用户模型，继承于AbstractUser
    用户
    """
    male, male = range(2)
    GENDER = (
        ('male', u"男"),
        ('female', u"女")
    )
    nickname = models.CharField(max_length=30,
                                null=False, blank=False, verbose_name=u"昵称")
    # 与旅游证件保持一致
    first_name = models.CharField(max_length=30,
                            null=True, blank=True, verbose_name=u"名")
    # 与旅游证件保持一致
    last_surname = models.CharField(max_length=30,
                               null=True, blank=True, verbose_name=u"姓")
    country_region = models.ForeignKey(Country, max_length=30, on_delete=models.PROTECT,
                                       null=True, blank=True,
                                       verbose_name=u"国家/地区代码")
    birthday = models.DateField(null=True,
                                blank=True, verbose_name=u"出生年月")
    gender = models.CharField(max_length=64,
                              choices = GENDER)
    # 手机号设置为不可以修改 用于接受短信通知 自动显示在页面上并获取
    mobile = models.CharField(max_length=64,null=True,
                              blank=True, verbose_name=u"手机号码")
    # 用于接收凭证或者短信通知
    email = models.EmailField(max_length=100,
                              null=True, blank=True, verbose_name=u"邮箱")

    objects = MyUserManager()

    class Meta:
        verbose_name = "用户个人信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.

        :return: string
        """
        return "{0} {1}".format(self.first_name, self.last_surname)

    def get_short_name(self):
        """
        Return the first_name.

        :return: string
        """
        return self.first_name

    def activation_expired(self):
        """
        Check if user's activation has expired.

        :return: boolean
        """
        return self.date_joined + timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS) < timezone.now()

    def confirm_email(self):
        """
        Confirm email.

        :return: boolean
        """
        if not self.activation_expired() and not self.confirmed_email:
            self.confirmed_email = True
            self.save()
            return True
        return False

# TODO：需要设置一个用户类型的字段或者别，区分针对不同类别的用户可以访问的数据也不同
# 用户注册模型


# drf官网
# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from rest_framework.authtoken.models import Token
#
#
# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)



# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
# from django.db import models
# from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
# from django.contrib.auth import get_user_model
# User = get_user_model()
#
#
# class Book(models.Model):
#     """
#     定义了一个Book类，用于显示书名book_name
#     未指定主键，系统会自动添加
#     :params book_ame: str
#     :params date_public: str
#     :rtype :str
#     """
#     book_name = models.CharField(max_length=50, default='', null=True)
#     date_public = models.DateTimeField(
#         _('date published'),
#         default=timezone.now
#     )
#
#     # __str__函数和__unicode__函数对比
#     def __str__(self):
#         return self.book_name
#
