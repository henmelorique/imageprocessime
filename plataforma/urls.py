"""plataforma URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *

urlpatterns = [ 
	path('plataforma', home, name = 'plataforma'), 
	path('mean', mean, name = 'success'),
	path('mediana', mediana, name = 'success'),
	path('histograma', realce, name = 'success'),
	path('bilateral', bilateral, name = 'success'),
	path('agucamento', laplaciano, name = 'success'),
	path('media_output', media_output, name = 'success_mean'),
	path('mediana_output', mediana_output, name = 'success_mediana'),
	path('bilateral_output', bilateral_output, name = 'success_bilateral'),
	path('histograma_output', realce_output, name = 'success_realce'),
	path('agucamento_output', laplaciano_output, name = 'success_laplaciano'),
] 


if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT) 

