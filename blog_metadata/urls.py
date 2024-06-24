from django.urls import path

from . import views

urlpatterns = [
    path("test/", views.test_api),
    path("get-blog/", views.get_blog), # if page number is not provided
    path("get-blog/<int:current_page>/", views.get_blog), 
    path("get-routes/",views.get_routes), # if page number is not provided
    path("get-routes/<int:current_page>", views.get_routes),
    # fetch single blog by id
    path("get-blog-by-id/<int:id>", views.get_blog_by_id) 
]
