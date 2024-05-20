from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test_api),
    path("get-blog/", views.get_blog), # if page number is not provided
    path("get-blog/<int:current_page>/", views.get_blog), 
]
