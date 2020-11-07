from django.urls import path
from .views import *

app_name = 'pdf'

urlpatterns = [
    path('', CustomerList.as_view(), name='home'),
    path('pdf/<pk>/', customer_pdf_view, name='customer-pdf'),
    path('test-pdf/', render_pdf_view, name='test-pdf'),
]