from django.contrib import admin

from NST.models import Content
from NST.models import Style

from NST.forms import ContentForm
from NST.forms import StyleForm

# Register your models here.

admin.site.register(Content)
admin.site.register(Style)

