from django.contrib import admin
from drives.models import Folder, File

admin.site.register(Folder)
admin.site.register(File)