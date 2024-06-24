from django.http import JsonResponse, Http404
from rest_framework import status
import math

from .models import Blog
from .serializers import BlogMetaDataSerializer, RouteSerializer, ContentSerializer

# Global Variables

per_page = 10  # how much records I want per page

# Create your views here.


def test_api(request):
    return JsonResponse({"test": "API is functioning properly"})


# Get Blogs for Home Page


def get_blog(request, current_page=1):

    if request.method == "GET":

        total_data = Blog.objects.count()

        # __CHECK IF PAGE IS VALID__
        if math.ceil(total_data / per_page) < current_page:
            return JsonResponse(
                {"message": "Page out of bounds", "status": status.HTTP_400_BAD_REQUEST}
            )

        # __PAGES__
        # previous page
        if current_page == 1:
            prev_page = None
        else:
            prev_page = current_page - 1

        # next page
        if total_data - current_page * per_page <= 0:
            next_page = None
        else:
            next_page = current_page + 1

        # __HANDLE DATA__
        skip_data = (current_page * per_page) - per_page

        blogs = Blog.objects.all()[skip_data : skip_data + per_page]
        serializer = BlogMetaDataSerializer(blogs, many=True)

        return JsonResponse(
            {
                "prev_page": prev_page,
                "current_page": current_page,
                "next_page": next_page,
                "data": serializer.data,
                "status": status.HTTP_200_OK,
            }
        )


def get_routes(request, current_page=1):

    if request.method == "GET":
        total_data = Blog.objects.count()
        
        # __CHECK IF PAGE IS VALID__
        if math.ceil(total_data / per_page) < current_page:
            return JsonResponse(
                {"message": "Page out of bounds", "status": status.HTTP_400_BAD_REQUEST}
            )

        # __HANDLE DATA__
        skip_data = (current_page * per_page) - per_page

        blogs = Blog.objects.all()[skip_data : skip_data + per_page]
        serializer = RouteSerializer(blogs, many=True)

        return JsonResponse({"data": serializer.data, "status": status.HTTP_200_OK})
    
def get_blog_by_id(request, id):

    print(id)

    if request.method == "GET":
        try:
            blog = Blog.objects.get(id=id)
        except:
            raise Http404("Failed to fetch blog")
        
        serializer = ContentSerializer(blog)

        return JsonResponse({"data": serializer.data, "status": status.HTTP_200_OK})