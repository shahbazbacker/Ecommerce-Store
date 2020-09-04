from django import forms
from products.models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control", 'placeholder' :"enter your name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control", 'placeholder' :"enter your email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control", 'placeholder' :"Your Opinion"}))
    
    class Meta:
        model = Contact
        fields = '__all__'


# class LoginForm(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)


# class RegisterForm(forms.Form):
#     username = forms.CharField()
#     email = forms.EmailField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     password2 = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         super().clean()
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')
#         if password != password2:
#             raise forms.ValidationError('passwords must match')
#         return data

     
