# 登录表单，继承了 forms.Form 类
# 引入表单类
from django import forms


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
