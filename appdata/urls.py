from django.urls import path
from .views import CustomerComplainForm, CustomerComplainList,CustomerComplainCreate, CustomerTemplaplate

app_name= 'appdata'
urlpatterns = [
    path('form/', CustomerComplainForm.as_view(), name='Form_page'),
    path('list/', CustomerComplainList.as_view(), name='List_page'),
    path('create/', CustomerComplainCreate.as_view(), name='Create_page'),
    path('status/', CustomerTemplaplate.as_view(), name='myMSG'),
    ]
