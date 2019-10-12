from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User

@receiver(post_save, sender=User)
def create_user(sender, instance=None, created=False, **kwargs):
    # 首次创建才进行加密(修改的时候也会有save操作)
    # 其实有Bug，出现在修改密码的时候
    if created:
        password = instance.password
        instance.set_password(password)
        instance.save()


