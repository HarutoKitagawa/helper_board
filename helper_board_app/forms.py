from django import forms

from .models import Request, Reply

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['category', 'text', 'detail']
        labels = {
            'category': 'カテゴリー',
            'text': '要件の要約',
            'detail': '詳細',
            }
        
class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['text']
        labels = {'text': ''}