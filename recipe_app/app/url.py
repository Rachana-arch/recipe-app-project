from django.urls import path
from app import views

app_name = 'app'

urlpatterns= [
    path('create/', views.CreateUserView().as_view(), name='create'),
    path('token/', views.CreateTokenView().as_view(), name='token')
]