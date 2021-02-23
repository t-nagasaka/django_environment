# from django.forms import ModelForm
# from .models import UserInfo

# class UserInfoForm(ModelForm):
#     class Meta:
#         model = UserInfo
#         fields = ['user_id', 'password']

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')