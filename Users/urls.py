from django.urls import path
from . import views

app_name = 'User'
urlpatterns = [
    path('',views.UserHome,name="Userhome"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout")
]
