from django import forms
from .models import main_model,blog_post
class main_form(forms.ModelForm):# here we are having forms which is used to populate all the model fields
    password=forms.CharField(widget=forms.PasswordInput(render_value=False),required=True)
    confirm_password=forms.CharField(widget=forms.PasswordInput(render_value=False),required=True)
    user=forms.CharField(widget=forms.HiddenInput(),initial="patients")
    class Meta:
        model=main_model
        fields="__all__"
    
class Login(forms.Form):# this is for login requiring only two fields
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput())

class doctor_blogs(forms.ModelForm):# here is the form requiring for populating the model fields
    username=forms.CharField(widget=forms.HiddenInput(),initial="None")# here using username hidden field so that blogs of that doctor can be viewed
    options=[('Mental Health','Mental Health'),('Heart Disease','Heart Disease'),('Covid19','Covid19'),('immunization','immunization')]
    category=forms.ChoiceField(choices=options)# here using options creating categories for blogs
    class Meta:
        model=blog_post
        fields="__all__"
    