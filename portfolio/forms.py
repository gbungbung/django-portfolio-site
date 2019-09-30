
from django import forms
from django.contrib.auth import authenticate, get_user_model
from portfolio.models import Art, Hires, Cv

User = get_user_model()

class RegisterForm(forms.ModelForm):
    bio = forms.CharField(max_length=500)
    password2 = forms.CharField(label='confrim password', widget= forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'bio', 'password', 'password2']
        widgets= {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'})
        }

    def clean(self, *args, **kwargs):
        password= self.cleaned_data.get('password')
        password2= self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password must match')
        return super(RegisterForm, self).clean(*args, **kwargs)
        
       
class LoginForm(forms.Form):
    username = forms.CharField(label='username' ,widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={'class':'form-control'}))


    def clean(self, *args, **kwargs):
        username= self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username= username, password= password)
            if not user:
                raise forms.ValidationError('The user you are trying to log onto, does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Passoword is incorrect')
        return super(LoginForm, self).clean(*args, **kwargs)

class CvForm(forms.ModelForm):
    class Meta:
        model = Cv
        fields = ['title', 'organisation', 'description', 'period']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'organisation': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'period': forms.TimeInput(attrs={'class':'form-control'}),
            }

class UploadForm(forms.ModelForm):
    class Meta:
       model = Art
       fields = ['categorie', 'description', 'img', 'name', 'size', 'featured']
       widgets = {
           'categorie': forms.TextInput(attrs={'class':'form-control'}),
           'description': forms.Textarea(attrs={'class':'form-control'}),
           'img': forms.FileInput(attrs={'class':'form-control'}),
           'name': forms.TextInput(attrs={'class':'form-control'}),
           'size': forms.TextInput(attrs={'class':'form-control'}),
           }

class HireMe(forms.ModelForm):

    class Meta:
        model = Hires
        fields = ('name', 'subject', 'Your_email', 'message', 'time_chosen')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
            'Your_email': forms.EmailInput(attrs={'class':'form-control'}),
            'time_chosen': forms.TimeInput(attrs={'class':'form-control'}),
            }
