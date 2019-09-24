
from django.forms import ModelForm
from portfolio.models import Art, Hires

class Upload(ModelForm):
    class Meta:
       Model = Art
       field = '__all__'

class HireMe(ModelForm):
    class Meta:
        model = Hires
        fields = '__all__'