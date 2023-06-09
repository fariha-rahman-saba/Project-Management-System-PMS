from django import forms
from .models import Project, Comment


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('title', 'title_tag', 'author', 
		          'body', 'snippet', 'header_image')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'saba', 'type': 'hidden'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.TextInput(attrs={'class': 'form-control'}),
		}


class EditForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('title', 'title_tag', 'body', 'snippet')

		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),
			'snippet': forms.TextInput(attrs={'class': 'form-control'}),
		}


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class': 'form-control'}),
			'body': forms.Textarea(attrs={'class': 'form-control'}),

		}
