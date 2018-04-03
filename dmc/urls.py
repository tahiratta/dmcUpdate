from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('certificate/', views.certificate, name='certificate'),
    path('careers/', views.careers, name='careers'),
    path('dmcmarkets/portal/document/s2k45/dfery35634345y4/resumes/pdfs/65149845/', views.pdfs, name='pdfs'),
    path('marketWatch/', views.marketWatch, name='marketWatch'),

]