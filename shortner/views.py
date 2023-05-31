from django.shortcuts import render
from uuid import uuid4
from .models import Url


def index(request):
    url = request.POST.get('url')
    if url:
        if request.method == 'POST':
            uid = str(uuid4())[:5]
            new_url = Url.objects.create(link=url, uuid=uid)
            new_url.save()
            context = {
                'new_url': new_url,
            }
            return render(request, 'index.html', context)
    return render(request, 'index.html')