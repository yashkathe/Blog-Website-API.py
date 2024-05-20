from django.http import JsonResponse
from rest_framework import status
import math

from .models import BlogMetaData
from .serializers import BlogMetaDataSerializer

# Global Variables

per_page = 10  # how much records I want per page

# Create your views here.


def test_api(request):
    return JsonResponse({"test": "API is functioning properly"})


# Get Blogs for Home Page


def get_blog(request, current_page = 1):

    if request.method == "GET":

        total_data = BlogMetaData.objects.count()

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

        blogs = BlogMetaData.objects.all()[skip_data : skip_data + per_page]
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
