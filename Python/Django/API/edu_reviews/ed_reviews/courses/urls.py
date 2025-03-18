from django.urls import path
from .views import (
    ListCreateCourse, 
    RetrieveUpdateDestroyCourse,
    ListCreateReview,
    RetrieveUpdateDestroyReview,

)

urlpatterns = [
    path('', ListCreateCourse.as_view(), name='course_list'),
    path('<pk>/', RetrieveUpdateDestroyCourse.as_view(), name='course_detail'),
    path('<course_pk>/reviews/', ListCreateReview.as_view(), name='review_list'),
    path('<course_pk>/reviews/<pk>/', RetrieveUpdateDestroyReview.as_view(), name='review_detail'),
]
