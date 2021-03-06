# Generated by Django 2.2.5 on 2019-10-09 13:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20191009_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(default='', max_length=50, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(default='', max_length=50, null=True, verbose_name='Last Name')),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('mobile', models.CharField(default='', max_length=50, null=True, verbose_name='Mobile')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]
