from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
import cv2
import numpy as np
import os
from matplotlib import pyplot as plt


# Create your views here. 
def home(request): 
	return render(request, 'index.html') 

def mean(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success_mean') 
	else: 
		form = HotelForm() 
	return render(request, 'media.html', {'form' : form}) 

def mediana(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success_mediana') 
	else: 
		form = HotelForm() 
	return render(request, 'mediana.html', {'form' : form}) 

def bilateral(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success_bilateral') 
	else: 
		form = HotelForm() 
	return render(request, 'bilateral.html', {'form' : form}) 


def realce(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success_realce') 
	else: 
		form = HotelForm() 
	return render(request, 'realce.html', {'form' : form}) 

def laplaciano(request): 

	if request.method == 'POST': 
		form = HotelForm(request.POST, request.FILES) 

		if form.is_valid(): 
			form.save() 
			return redirect('success_laplaciano') 
	else: 
		form = HotelForm() 
	return render(request, 'agucamento.html', {'form' : form}) 

def media_output(request): 
	if request.method == 'GET': 
		n = Hotel.objects.count()
		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all()[n-1:]
		a = Hotels[0].hotel_Main_Img.url
		b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ a
		image = cv2.imread(b)

		blur = cv2.blur(image,(5,5))
		c = cv2.imwrite('/home/henrique/plataforma/media/images/blur.jpg', blur)
		return render(request, 'media_output.html')

def mediana_output(request): 
	if request.method == 'GET': 
		n = Hotel.objects.count()
		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all()[n-1:]
		a = Hotels[0].hotel_Main_Img.url
		b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ a
		image = cv2.imread(b)

		mediana = cv2.medianBlur(image,5)
		c = cv2.imwrite('/home/henrique/plataforma/media/images/mediana.jpg', mediana)
		return render(request, 'mediana_output.html')

def bilateral_output(request): 
	if request.method == 'GET': 
		n = Hotel.objects.count()
		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all()[n-1:]
		a = Hotels[0].hotel_Main_Img.url
		b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ a
		image = cv2.imread(b)

		bilateral = cv2.bilateralFilter(image,9,75,75)
		c = cv2.imwrite('/home/henrique/plataforma/media/images/bilateral.jpg', bilateral)
		return render(request, 'bilateral_output.html')


def realce_output(request): 
	if request.method == 'GET': 
		n = Hotel.objects.count()
		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all()[n-1:]
		a = Hotels[0].hotel_Main_Img.url
		b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ a
		image = cv2.imread(b)

		img_to_yuv = cv2.cvtColor(image,cv2.COLOR_BGR2YUV)
		img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
		equ = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
		c = cv2.imwrite('/home/henrique/plataforma/media/images/realce.jpg', equ)
		return render(request, 'realce_output.html')

def laplaciano_output(request): 
	if request.method == 'GET': 
		n = Hotel.objects.count()
		# getting all the objects of hotel. 
		Hotels = Hotel.objects.all()[n-1:]
		a = Hotels[0].hotel_Main_Img.url
		b = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+ a
		image = cv2.imread(b)
	
		kernel_sharpening = np.array([[-1,-1,-1], 
                              		      [-1, 9,-1],
                              		      [-1,-1,-1]])
		sharpened = cv2.filter2D(image, -1, kernel_sharpening)

		#laplacian = cv2.Laplacian(image,cv2.CV_64F)
		c = cv2.imwrite('/home/henrique/plataforma/media/images/laplaciano.jpg', sharpened)
		return render(request, 'agucamento_output.html')




