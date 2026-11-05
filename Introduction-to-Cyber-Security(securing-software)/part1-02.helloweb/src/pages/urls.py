from django.urls import path

from .views import homePageView, add, multiply

urlpatterns = [
    path('',          homePageView, name='home'),
    # path('add/',      add,          name='add'),
    # path('multiply/', multiply,     name='multiply')
]
