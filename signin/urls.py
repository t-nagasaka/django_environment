from django.urls import path
from . import views

app_name = 'signin'
urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),
    # path('signup/', views.signup, name='signup'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]