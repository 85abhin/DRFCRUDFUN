from django.urls import path
from myapp import views
urlpatterns = [
    path('studentinfo/', views.student_api),
    path('studentinfo/<int:pk>', views.student_api),
    
]