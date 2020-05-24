from django import forms 
from .models import * 
class PhotoToBeMeasuredForm(forms.ModelForm):
    class Meta:
        model = PhotoToBeMeasured
        fields = ['left_most_width', 'main_photo']
