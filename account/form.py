from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
from account.models import Address, User


class RegisterForm(forms.Form):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'cs_form_field' , 'placeholder':' شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)] , required=True)

    def clean_phone(self):
      phone = self.cleaned_data.get("phone")
      if len(phone)<11:
          raise ValidationError("This Information is not correct")
      return phone

class OtpForm(forms.Form):
    code = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'cs_form_field' , 'placeholder':'کد ارسال شده :'}) , validators=[validators.MaxLengthValidator(4)])
    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox , required = True)
    def clean_code(self):
        code = self.cleaned_data.get("code")
        if len(code)<4:
            raise ValidationError("this code is invalid")
        return code

class Edite_Profile_Form(forms.ModelForm):
    phone = forms.CharField(widget = forms.TextInput(attrs={'class': 'cs_form_field' , 'placeholder':'شماره تلفن'}) , validators=[validators.MaxLengthValidator(11)] , required=False)
    class Meta:
        model=User
        fields=['Full_name', 'username' , 'email' , 'phone' , 'image']
        widgets={
            'username':forms.TextInput(attrs={'class': 'cs_form_field' , 'placeholder':'نام کاربری'}),
            'Full_name' :forms.TextInput(attrs={'class': 'cs_form_field' , 'placeholder':'نام و نام خانوادگی'}),
            'email' :forms.TextInput(attrs={'class': 'cs_form_field' , 'placeholder':'ایمیل'}),
        }

class AddressCreationForm(forms.ModelForm):
    user = forms.IntegerField(required=False)
    class Meta:
        model = Address
        exclude = '__all__'