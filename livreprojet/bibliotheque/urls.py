from django.urls import path
from . import views

urlpatterns = [
    path('ajout/', views.ajout, name="ajout"),
    path('liste/', views.liste, name="liste"),
    path('affiche/<int:id>/', views.read, name="read"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
]
