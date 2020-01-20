from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#     class Meta():
#         model = User
#         fields = ('username','password','email')
        
# class UserProfileInfoForm(forms.ModelForm):
#      class Meta():
#          model = UserProfileInfo
#          fields = ('profile_pic')

# class RegisterForm(UserCreationForm):
#     # declare the fields you will show
#     username = forms.CharField(label="نام کاربری")
#     # first password field
#     password1 = forms.CharField(label="رمز عبور")
#     # confirm password field
#     password2 = forms.CharField(label="تکرار رمز عبور")
#     email = forms.EmailField(label = "ایمیل")
#     first_name = forms.CharField(label = "نام شما")
#     last_name = forms.CharField(label = "فامیلی شما")
 
#     # this sets the order of the fields
#     class Meta:
#         model = User
#         fields = ("first_name", "last_name", "email", "username", "password1", "password2", )
 
#     # this redefines the save function to include the fields you added
#     def save(self, commit=True):
#         user = super(RegisterForm, self).save(commit=False)
#         user.email = self.cleaned_data["email"]
#         user.first_name = self.cleaned_data["first_name"]
#         user.last_name = self.cleaned_data["last_name"]
#         if commit:
#             user.save()
#             return user                