from django.urls import path

from . import views

app_name = 'posts'

urlpatterns = [
    path("", views.AllPosts.as_view(), name="all"),
    path("new/", views.CreatePost.as_view(), name="create"),
    path(
        "by/<username>/",
        views.UserPosts.as_view(),
        name="for_user"
    ),
    path(
        "by/<username>/<pk>/",
        views.SinglePost.as_view(),
        name="single"
    ),
    path(
        "delete/<pk>/",
        views.DeletePost.as_view(),
        name="delete"
    ),
]
