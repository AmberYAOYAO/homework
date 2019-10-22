from django import forms
from django.forms import ModelForm
from Foods.models import Foods

class UserForm(forms.Form):
    username = forms.CharField(max_length=12,min_length=6)
    password = forms.CharField(
        max_length=12,#最大长度
        min_length=6, #最小长度
        widget=forms.PasswordInput(attrs={"class":"title"}),#样式和属性
        required=True,#是否可以为空
        label="密码",#前端label标签提升内容
        error_messages={"required":"密码不可以为空"}#错误信息



    )

class FoodsForm(ModelForm):
     class Meta:
         model = Foods
         fields = "__all__"
         # fields = ("name","price","picture","description")
         labels = {
             "name":"食品名称",
             "price":"食品价格",
             "picture":"食品图片",
             "description":"食品描述",
             "type_id":"食品类型"

         }
def clean_name(self):
    pool = ["admin","aaa"]
    name = self.cleaned_data.get("name")
    if name in pool:
        self.add_error("name","非法命名")
    else:
        return name