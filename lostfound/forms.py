from django import forms
from .models import LostFoundItem

class LostFoundItemForm(forms.ModelForm):
    class Meta:
        model = LostFoundItem
        fields = ['title', 'category', 'description', 'location', 'status']
        widgets = {
            'category': forms.TextInput(attrs={
                'placeholder': 'e.g. Phone, Charger, Bag',
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

# from django import forms
# from .models import LostFoundItem

# class LostFoundItemForm(forms.ModelForm):
#     class Meta:
#         model = LostFoundItem
#         fields = ['title', 'description', 'location', 'status']
