from django.http import HttpResponse


# Create your views here.

def addPageView(request):
	first  = int(request.GET.get('first'))
	second = int(request.GET.get('second'))
	res = first + second
	return HttpResponse(res)
	

def multiplyPageView(request):
	first  = int(request.GET.get('first'))
	second = int(request.GET.get('second'))
	res = first * second
	return HttpResponse(res)
