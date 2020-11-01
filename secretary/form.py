from django import forms
from . models import Partner


class PartnerForm(forms.ModelForm):
    
    class Meta:
        model = Partner 
        fields = ('person','number','pilot','date_admission','act_number','type','club','presenter_1','presenter_2','user','group')
        labels = {
            'person':'Nombre',
        }
    
    def __init__(self, *args, **kwargs):
        super(PartnerForm, self).__init__(*args, **kwargs)
        self.fields['person'].empty_label = 'Seleccionar'
        self.fields['pilot'].empty_label = 'Seleccionar'
        self.fields['type'].empty_label = 'Seleccionar'
        self.fields['club'].empty_label = 'Seleccionar'
        self.fields['user'].empty_label = 'Seleccionar'
        self.fields['group'].empty_label = 'Seleccionar'
        