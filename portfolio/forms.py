from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from .models import Profile, Resume, Art, Hires

User = get_user_model()

class RegisterForm(forms.ModelForm):
    prof_pic= forms.ImageField(label='Image', widget= forms.FileInput(attrs={'class':'form-control'}))
    bio = forms.CharField(max_length=500, label='Biography', widget= forms.Textarea(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='confrim password', widget= forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model= User
        fields= ['username', 'first_name', 'last_name', 'email', 'bio', 'prof_pic', 'password', 'password2']
        widgets= {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
        }

    #Check if the password submitted are same
    def clean(self, *args, **kwargs):
        password= self.cleaned_data.get('password')
        password2= self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError('Password must match')
        return super(RegisterForm, self).clean(*args, **kwargs)

class LoginForm(forms.Form):
    username = forms.CharField(label='username' ,widget= forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Password', widget= forms.PasswordInput(attrs={'class':'form-control'}))

    #Check if the password submitted are same
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

class ResumeForm(forms.ModelForm):
    options = (
        ('WD', 'Work experience'),
        ('3D', 'Education'),
        )
    categorie = forms.ChoiceField(required=False)

    class Meta:
        model = Resume
        fields = ['title', 'organisation', 'description', 'start_date', 'end_date']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'organisation': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control'}),
            'end_date': forms.DateInput(attrs={'class':'form-control'}),
            'categorie': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
            }

class ArtForm(forms.ModelForm):
    options = (
        ('WD', 'Web design'),
        ('3D', '3D design'),
        ('Prints', 'Photographs and prints'),
        )
    categorie = forms.ChoiceField(label='Category', choices=options,)

    class Meta:
        model= Art
        fields= ['title', 'categorie', 'img', 'description', 'featured']
        widgets= {
            'categorie': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
        }

class HireForm(forms.ModelForm):
    options = (
        ('WD', 'Web design'),
        ('3D', '3D design'),
        ('Prints', 'Photographs and prints'),
        )
    subjects = forms.ChoiceField(choices=options, required=False)

    class Meta:
        model = Hires
        fields= ['name', 'Your_email', 'message','subjects' ]
        widgets= {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'Your_email': forms.EmailInput(attrs={'class':'form-control'}),
            'message': forms.Textarea(attrs={'class':'form-control'}),
            'subjects': forms.CheckboxSelectMultiple(attrs={'class':'form-control'}),
            }