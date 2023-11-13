from django.forms import ModelForm
from .models import Jurnal

class JurnalForms(ModelForm):
  class Meta:
    model = Jurnal
    fields = '__all__'