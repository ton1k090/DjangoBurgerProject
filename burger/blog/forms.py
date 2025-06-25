from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    '''Форма для написания комментрариев'''
    class Meta:
        model = Comment
        fields = ('text', 'name')
        widgets = {
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст вашего комментария'
            }
            ),
            'name': forms.TextInput(attrs={'class': 'form-control',
                                           'placeholder': 'Ваше имя'})
        }