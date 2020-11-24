from django import forms 
from .models import Content
from .models import Style
  
class ContentForm(forms.ModelForm): 
    
    class Meta: 
        model = Content
        fields = ['content'] 

class StyleForm(forms.ModelForm): 
    
    class Meta: 
        model = Style
        fields = ['style'] 
