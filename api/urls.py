from django.urls import path, re_path
from api import views

urlpatterns = [
    path('login/', views.login),
    path('logout/', views.logout),
    path('Users/', views.UserList.as_view()),
    path('Reviews/',views.ReviewView.as_view())

]

