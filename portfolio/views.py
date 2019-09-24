from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from portfolio.models import DesignerDetails, Art, Hires
from portfolio.forms import HireMe, Upload

class Home(View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwarg):
        details = DesignerDetails.objects.all()
        arts = Art.objects.filter(featured= True)
        return render(request, self.template_name, {'title':'Homepage', 'details':'details', 'art':'arts'})

class Myart(View):
    form_class = Upload
    template_name= 'gridprojects.html'

    def get(self, request, *arg, **kwarg):
        arts = Art.objects.all().order_by()
        return render(request, self.template_name, {'title':'Photograph and prints', 'art':'art'})

    def post(self, request, id):
        designer = get_designer(request.user) #Instance user have to be defined. I'll define after adding register button
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.instance.designer= designer 
            form.save()
            return redirect(reverse('art-details', parmanent= True, kwarg={'id':self.instance.id} ))

class Hire(View):
    form_class = HireMe
    template_name = 'hireme.html'
    hires = 'hires.html'

    def get(self, request, *arg, **kwarg):
        if request.user.is_authenticated:
            data = Hires.objects.all().order_by('-time')
            return render(request, self.hires, {'title':'Hires', 'message':'data'})
        else:
            form = HireMe()
        return render(request, self.template_name, {'title':'Hire'})

    def post(self, request, *arg, **kwarg):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['Email']
            form.save()
            return redirect('/success/')


