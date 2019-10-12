# from django.contrib import admin
# from accounts.models import Book
#
# # 2.0以上使用装饰器
# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display=('id', 'book_name', 'date_public')
#
# admin.site.unregister(Book)
# admin.site.register(Book, BookAdmin)
#
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from accounts.models import User
#
# admin.site.register(User, UserAdmin)

from django.contrib import admin
from accounts.models import User, TourToken

# 2.0以上使用装饰器
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display=('id', 'nickname', 'first_name', 'last_surname',
    #               # 'country_region',
    #               'birthday', 'gender', 'mobile',  'email')
    list_display=( 'nickname', 'mobile')


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# 2.0以上使用装饰器
@admin.register(TourToken)
class TourTokenAdmin(admin.ModelAdmin):
    list_display=('id', 'user', 'token')

admin.site.unregister(TourToken)
admin.site.register(TourToken, TourTokenAdmin)