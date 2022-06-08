from email.policy import HTTP
from django.shortcuts import render, redirect
import uuid
from .models import UrlLink
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        url = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = UrlLink(link=url, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def result(request, pk):
    url_details = UrlLink.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)