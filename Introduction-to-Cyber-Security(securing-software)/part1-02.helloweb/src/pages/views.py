from django.http import HttpResponse


# Create your views here.
# def add(request):
#     first  = int(request.GET.get('first'))
#     second = int(request.GET.get('second'))
#     res = first + second
#     return HttpResponse(res)


# def multiply(request):
#     first  = int(request.GET.get('first'))
#     second = int(request.GET.get('second'))
#     res = first * second
#     return HttpResponse(res) 


def homePageView(request):
    return HttpResponse("Hello Web!")