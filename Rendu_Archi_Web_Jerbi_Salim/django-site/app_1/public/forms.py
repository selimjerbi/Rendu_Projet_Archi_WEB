from django import forms
from api.models import Service
from api.models import IntegrationWeekend

class ServiceForm(forms.ModelForm):
    name = forms.CharField(label='Service', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    price = forms.DecimalField(label='Prix', max_digits=10, decimal_places=2)

    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

    def __init__(self, *args, **kwargs):
        super(ServiceForm, self).__init__(*args, **kwargs)
        self.fields['name'].initial = self.instance.name  # initialiser le champ 'service' avec la valeur de 'name'
        self.fields['name'].widget.attrs['placeholder'] = 'Entrez le nom du service'

class UpdateDescriptionForm(forms.ModelForm):
    class Meta:
        model = IntegrationWeekend
        fields = ['description'] 