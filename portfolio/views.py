from django.views import View
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import login, logout, authenticate, get_user_model

User = get_user_model()

from .forms import RegisterForm, LoginForm, ArtForm, HireForm, ResumeForm
from .models import Profile, Art, Hires, Resume

class Register(View):
    template_name= 'register.html'
    form_class = RegisterForm

    def get(self, request, *arg, **kwarg):
        form = self.form_class()
        return render(request, self.template_name, {'title':'Register', 'form':form})

    def post(self, request, *arg, **kwarg):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            #user.refresh_from_db() will hard refresh db hence help to retrieve the instance user, it is used because of signals used which cause synchronism
            password= form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user =  authenticate(username=user.username, password= password)
            login(request, new_user)
            return redirect('/')
        return render(request, self.template_name, {})
    
class Login(View):
    template_name= 'signin.html'
    form_class= LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'titlte':'Login','form':form})

    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST)
        if form.is_valid():
            username= form.cleaned_data.get('username')
            password= form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        return render(request, self.template_name, {'form':form})

class Home(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        details = Profile.objects.all()
        arts = Art.objects.all()[:3]
        return render(request, self.template_name, {'title':'Homepage', 'details':details, 'arts':arts})

#Shows arts grid, almost all
class Arts(View):
    template_name= 'gridprojects.html'

    def get(self, request, *args, **kwargs):
        arts = Art.objects.all()
        return render(request, self.template_name, {'title':'Projects', 'arts':arts})

#Showing art post with details
class ArtDetail(View):
    template_name = 'project.html'

    def get(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        arts = Art.objects.all()[:4]
        return render(request, self.template_name, {'title':'Detail', 'art':art, 'arts':arts})

#Adding arts to the database
class   AddArt(View):
    template_name= 'upload.html'
    form_class= ArtForm

    def get(self, request, *args, **kwargs):
        form= self.form_class()
        return render(request, self.template_name, {'title':'Add Art', 'heading':'Create', 'form':form})

    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio:artdetail', kwargs={'pk':form.instance.pk}))
        return render(request, self.template_name, {})

class EditArt(View):
    template_name= 'upload.html'
    form_class= ArtForm

    def get(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        form= self.form_class(instance=art)
        return render(request, self.template_name, {'title':'Add Art', 'heading':'Edit', 'form':form})

    def post(self, request, pk):
        art = get_object_or_404(Art, pk=pk)
        form= self.form_class(request.POST or None, request.FILES or None, instance=art)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio:artdetail', kwargs={'pk':form.instance.pk}))
        return render(request, self.template_name, {})

class ArtDelete(View):
    def get(self, request, pk):
        get_object_or_404(Art, pk=pk).delete()
        return redirect(reverse('portfolio:projects'))

class Hire(View):
    template_name= 'hireme.html'
    form_class= HireForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            hires = Hires.objects.all()
            return render(request, 'hires.html', {'title':'Hires', 'hires':hires})
        else:
            form = self.form_class()
        return render(request, self.template_name, {'title':'Hire', 'form':form})

    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio:Home'))
        return render(request, self.template_name, {})

class Resumee(View):
    template_name= 'resume.html'

    def get(self, request, *args, **kwargs):
        cv = Resume.objects.all()
        dat = Profile.objects.all()
        return render(request, self.template_name, {'title':'Resume', 'cv':cv, 'data':dat})

class Resumee_add(View):
    form_class= ResumeForm
    template_name= 'cvadd.html'

    def get(self, request, *args, **kwargs):
        form= self.form_class()
        return render(request, self.template_name, {'title':'Add resume', 'form':form, 'data':'Create'})

    def post(self, request, *args, **kwargs):
        form= self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio:resume'))
        return render(request, self.template_name, {})

class Resumee_detail(View):
    template_name= 'cvdetail.html'

    def get(self, request, pk):
        cvs = get_object_or_404(Resume, pk=pk)
        return render(request, self.template_name, {'title':'Resumedetail', 'cvs':cvs, })

class Resumee_edit(View):
    form_class= ResumeForm
    template_name= 'cvadd.html'

    def get(self, request, pk):
        cv = get_object_or_404(Resume, pk=pk)
        form = self.form_class(instance=cv)
        return render(request, self.template_name, {'title':'Resume edit', 'form':form, 'data':'Edit'})

    def post(self, request, pk):
        cv = get_object_or_404(Resume, pk=pk)
        form = self.form_class(request.POST or None, instance=cv)
        if form.is_valid():
            form.save()
            return redirect(reverse('portfolio:resume'))
        return render(request, self.template_name, {})

class Resume_delete(View):
    def get(self, request, pk):
        get_object_or_404(Resumee, pk=pk).delete()
        return redirect(reverse('portfolio:resume'))