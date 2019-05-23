from django import forms
from .models import Comment
class CommentForm(forms.Form):
    name = forms.CharField(label='输入姓名', required=True, widget=forms.TextInput(attrs={'id': 'id_name'}))
    email = forms.EmailField(label='输入邮箱',required=True,  widget=forms.EmailInput(attrs={'id':'id_email'}))
    url = forms.URLField(label='输入个人主页', widget=forms.URLInput(attrs={'id':'id_url'}))
    comment = forms.CharField(label='输入评论', required=True, widget=forms.Textarea(attrs={'id':'id_comment'}))