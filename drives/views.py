from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from .models import Folder, File
from .forms import FolderForm, FileForm
from django.contrib.auth.decorators import login_required

def index(request):
	return render(request, 'drives/index.html')

@login_required
def folders(request):
	folders = Folder.objects.filter(owner=request.user).order_by('date_added')
	context = {'folders': folders}
	return render(request, 'drives/folders.html', context)

@login_required
def folder(request, folder_id):
	folder = Folder.objects.get(id=folder_id)
	files = folder.file_set.order_by('-date_added')
	if folder.owner != request.user:
		raise Http404
	context = {'folder': folder, 'files': files}
	return render(request, 'drives/folder.html',context)

@login_required
def new_folder(request):
	if request.method != 'POST':
		form = FolderForm()
	else:
		form = FolderForm(request.POST)
		if form.is_valid():
			new_folder = form.save(commit=False)
			new_folder.owner = request.user
			new_folder.save()
			return HttpResponseRedirect(reverse('drives:folders'))

	context = {'form': form}
	return render(request,'drives/new_folder.html', context)

@login_required
def upload(request, folder_id):
	folder = Folder.objects.get(id=folder_id)

	if request.method != 'POST':
		form = FileForm()
	else:
		form = FileForm(data=request.POST)
		if form.is_valid():
			upload = form.save(commit=False)
			upload.Folder = folder
			upload.save()
			return HttpResponseRedirect(reverse('drives:folder', args=[folder_id]))
	context = {'folder': folder, 'form': form}
	return render(request, 'drives/upload.html', context)