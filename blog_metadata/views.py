from django.http import JsonResponse
from .models import BlogMetaData
from .serializers import BlogMetaData

# Create your views here.

def test_api(request):
    return JsonResponse({"test": "API is functioning properly"})

    
