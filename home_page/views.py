from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_page(request):

    hostname = request.get_host()

    reponse_text = f"The routes start from api/ \n1. test \n2. get-blog \n3. get-blog-by-id"
    return HttpResponse(reponse_text, content_type='text/plain')