from django import forms
from .models import Folder, File

class FolderForm(forms.ModelForm):
	class Meta:
		model = Folder
		fields = ['name']
		labels = {'name': '文件夹名称'}

class FileForm(forms.ModelForm):
	class Meta:
		model = File
		fields = ['name', 'link']
		labels = {'name': '文件名', 'link': '文件的内容或文件的链接'}
		widgets = {'link': forms.Textarea(attrs={'cols': 80})}