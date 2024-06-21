from django import forms
from .models import  Post, profile

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['job_title', 'company_name', 'location', 'description', 'posted_date']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['profile_image', 'firstname', 'lastname', 'bio', 'resume']
