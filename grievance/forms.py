from django import forms

from .models import Comment, Post

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','text','created_date','author')
