from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('get-started/', views.get_started, name='get_started'),
    path('for-business/', views.for_business, name='for_business'),
    path('careers/', views.careers, name='careers'),  # NEW
    path('api/submit-interest/', views.submit_interest, name='submit_interest'),
]