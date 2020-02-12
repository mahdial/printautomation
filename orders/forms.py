from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django import forms
from .models import orders, customers, Templates, DasteMahsool
from jalali_date.fields import JalaliDateField, SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime

class Order_Form(ModelForm):
    class Meta:
        model = orders
        fields = '__all__'
        #Name_Moshtari = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
        widgets = {
            'Name_Moshtari': forms.TextInput(attrs={'class': 'AutoComp'}),
            'Daste_Mahsool': forms.TextInput(attrs={'class': 'AutoComp'}),
            'MavadAvaliye1': forms.TextInput(attrs={'class': 'AutoComp'}),
            'CodeGhaleb': forms.TextInput(attrs={'class': 'AutoComp'}),
        }