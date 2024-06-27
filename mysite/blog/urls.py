from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_rating, name = 'home'),
    path('form/', views.forms, name = 'form'),
    path('accept/', views.accept, name = 'accept'),
    path('graduate/', views.graduate, name = 'graduate'),
    path('scoreaccept/', views.score_accept, name = 'scoreaccept'),
    path('choice/', views.choice_project, name = 'choice'),
    path('form_init/', views.form_init, name = 'init'),
    path('accept_init/', views.accept_init, name='accept_init')
]