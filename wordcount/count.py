from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
 	return render(request,"home.html")


def counter(request):
	name = request.GET['First']+' '+request.GET['Last']
	gender = request.GET['Gender']
	email = request.GET['Email ID']
	return render(request,"Count-page.html",{'name':name,'gender':gender,'email':email})
	

def	countvalue(request):
	fulltext = request.GET['fulltext']
	return render(request,"count.html",{'fulltext':fulltext})


