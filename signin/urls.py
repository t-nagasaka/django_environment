from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'signin'
urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('', auth_views.LoginView.as_view(template_name="signin/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page="about:index"), name='logout'),
]