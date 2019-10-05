from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth import authenticate, get_user_model, login

from portfolio.forms import HireMe, RegisterForm, LoginForm, UploadForm, CvForm
from portfolio.models import Art, Hires, Profile, Cv

User = get_user_model()

def get_designer(User):
    qs = Designer.objects.filter(User=user)
    if qs.exist():
        return qs[0]
    return None

class Home(View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwarg):
        details = Profile.objects.all().filter(user_id=2)
        arts = Art.objects.filter(featured= True)
        return render(request, self.template_name, {'title':'Homepage', 'details':details, 'art':arts})

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
            user.refresh_from_db()     #This will hard refresh db hence help to retrieve the instance user, it is used because of signals used which cause synchronism
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

class Resume(View):
    model = Cv
    form_class = CvForm
    template_name = 'resume.html'

    def get(self, request, *args, **kwargs):
        details = Profile.objects.all().filter(user_id=2)
        cv = Cv.objects.all()
        return render(request, self.template_name, {'title':'Resume', 'details':details, 'cv':cv})

class Resume_add(View):
    template_name= 'cvadd.html'
    form_class = CvForm

    def get(self, request, *args, **kwargs):
        form= self.form_class()
        return render(request, self.template_name, {'title':'Add resume details', 'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {'title':'Add resume details'})

class Resume_edit(View):
    form_class = CvForm
    template_name= 'cvadd.html'

    def get(self, request, pk):
        cv= get_object_or_404(Cv, pk=pk)
        form = self.form_class(instance=cv)
        return render(request, self.template_name, {'title':'Edit resume', 'form':form})

    def post(self, request, pk):
        cv= get_object_or_404(Cv, id=id)
        form = self.form_class(request.POST or None, instance=cv)
        if form.is_valid():
            cv = form.save()
            return redirect('/')
        return render(request, self.template_name, {})

class Resume_delete(View):
    template_name= 'cvadd.html'
    form_class = CvForm

    def cv_delete(self, request, *args, **kwargs):
        cv = get_object_or_404(Cv, pk=pk)
        cv.delete()
        return redirect('/')

class Myart(View):
    template_name= 'gridprojects.html'

    def get(self, request, *arg, **kwarg):
        arts = Art.objects.all()
        return render(request, self.template_name, {'title':'Photograph and prints', 'art':arts})

class ArtDetail(View):
    model = Art
    template_name = 'project.html'

    def get(self, request, *args, **kwargs):
        details = Art.object.all()
        return render(request, self.template_name, {'details':details})

class Upload(View):
    form_class = UploadForm
    template_name = 'upload.html'

    def get(self, request, *arg, **kwarg):
        form = self.form_class()
        return render(request, self.template_name, {'title':'Upload', 'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        designer = get_designer(request.user)
        if form.is_valid():
            form.instance.designer= designer
            form.save()
            return redirect(reverse('artdetail', kwargs={'id':form.instance.id} ))
        return render(request, self.template_name, {'form':form})

class Hire(View):
    form_class = HireMe
    template_name = 'hireme.html'
    hires = 'hires.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            data = Hires.objects.all().order_by('id')
            return render(request, self.hires, {'title':'Hires', 'data':data})
        else:
            form = self.form_class()
        return render(request, self.template_name, {'title':'Hire', 'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {})


