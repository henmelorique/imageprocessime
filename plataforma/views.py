from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
import cv2
import numpy as np

# Create your views here. 
def hotel_image_view(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success') 
	else: 
		form = HotelForm() 
	return render(request, 'index.html', {'form' : form}) 


def results(request): 
	if request.method == 'GET': 
		
		# getting all the objects of hotel. 
		Hotels = Hotel.objects.earliest('hotel_Main_Img')
		#image = cv2.imread(Hotels)
		#blur = cv2.blur(Hotels,(5,5))
		return HttpResponse(render(request, 'display.html', {'hotel_images' : Hotels}))



