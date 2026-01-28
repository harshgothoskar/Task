from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('qa/', views.qa_view, name='qa'),
]
