from .models import *
from django.forms import ModelForm

class InfoForm(ModelForm):
    class Meta:
        model = Info
        fields = '__all__'