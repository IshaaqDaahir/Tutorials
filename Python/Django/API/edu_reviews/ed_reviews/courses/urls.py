from django.urls import path
from .views import ListCreateCourse

app_name = 'courses'

urlpatterns = [
    path('', ListCreateCourse.as_view(), name='course_list'),
]
