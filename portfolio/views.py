from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.core.mail import send_mail

from portfolio.models import DesignerDetails, Art
from portfolio.forms import ContactMe

class Home(View):
    template_name = 'index.html'

    def get(self, request, *arg, **kwarg):
        details = DesignerDetails.objects.all()
        arts = Art.objects.filter(featured= True)
        return render(request, self.template_name, {'title':'Homepage', 'details':'details', 'art':'arts'})

class Myart(View):
    template_name= 'gridprojects.html'

    def get(self, request, *arg, **kwarg):
        arts = Art.objects.all().order_by()
        return render(request, self.template_name, {'title':'Photograph and prints', 'art':'art'})

class Contact(View):
    form_class = ContactMe
    template_name = 'contact.html'
    home = 'index.html'

    def get(self, request, *arg, **kwarg):
        form =  ContactMe()
        return render(request, self.template_name, {'title':'Contact'})

    def post(self, request, *arg, **kwarg):
        form = self.form_class(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            sender = form.cleaned_data['your_email']
            message = form.cleaned_data['message']

            recipients = ['gbungbung@gmail.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/sent/')#how this works
        return render(request, self.home, {'title':'Sent'})