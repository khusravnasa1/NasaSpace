from django.urls import path
from . import views
from .controller import authview

urlpatterns = [
    path('', views.home, name='home'),

    path('open_science_projects', views.projects, name='researches'),
    path('register/', authview.register, name='register'),
    path('login/', authview.loginpage, name='loginpage'),
    path('logout/', authview.logoutpage, name='logout'),
    #path('submit_review/<int:research_id>/', views.submit_review, name='submit_review'),


]
