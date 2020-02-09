from django.forms import ModelForm
from .models import ProfileDetail
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class ProfileDetail_Form(ModelForm):
    class Meta():
        model = ProfileDetail
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProfileDetail_Form, self).__init__(*args, **kwargs)
        self.fields['birthday'] = JalaliDateField(label=_('birthday'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )

        # you can added a "class" to this field for use your datepicker!
        # self.fields['date'].widget.attrs.update({'class': 'jalali_date-date'})

        self.fields['date_time'] = SplitJalaliDateTimeField(label=_('date time'), 
            widget=AdminSplitJalaliDateTime # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
        )        

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