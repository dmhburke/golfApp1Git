from django import forms
from django.forms import ModelForm
from catalog.models import LaTourScoreModel
from catalog.choices import *

class LaTourScoreForm(ModelForm):
#    hole = forms.ModelChoiceField(queryset=HoleModel.objects.all())
    slot1_score = forms.IntegerField(label='', required=False)
    slot2_score = forms.IntegerField(label='', required=False)
    slot3_score = forms.IntegerField(label='', required=False)

    def __init__(self, *args, **kwargs):
        super(LaTourScoreForm, self).__init__(*args, **kwargs)
        self.fields['slot1_score'].widget.attrs={'class': 'scoreInput'}
        self.fields['slot2_score'].widget.attrs={'class': 'scoreInput'}
        self.fields['slot3_score'].widget.attrs={'class': 'scoreInput'}
    
    class Meta:
        model = LaTourScoreModel
        fields = ('slot1_score', 'slot2_score', 'slot3_score',)
