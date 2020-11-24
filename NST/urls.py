from django.contrib import admin
from django.urls import path,include
from django.conf import settings
#from .views import redirect_view
from django.conf.urls.static import static 
from NST import views
from NST import models
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from NST import forms
from .views import redirect_view
urlpatterns = [
    path('admin', admin.site.urls),
    path("", views.index, name='home'),
    path("index",views.index, name='index'),
    path("stylefunc", views.stylefunc, name="stylefunc"),
    path("contentfunc", views.contentfunc, name="contentfunc"),
    path("capturefunc", views.capturefunc, name="capturefunc"),
    path("contentdisplay/<path:pk_test>",views.contentdisplay, name="contentdisplay"),
    path("styledisplay/<path:pk_test>",views.styledisplay, name="styledisplay"),
    path("styledisplay/style/uploads/content/<path:pk_test>",views.changepath),
    path("content",views.content,name="content"),
    path("style",views.style,name="style"),
    path('/redirect/', redirect_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
