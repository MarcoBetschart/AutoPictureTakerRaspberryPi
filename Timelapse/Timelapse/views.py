from django.shortcuts import render
from Timelapse.models import TimelapseImage
from django.http import Http404


def index(request):
    return render(request, 'index.html')

def timelapseImg(request, imgId):
    img = TimelapseImage.objects.get(pk=imgId)
    if img is not None:
        return render(request, 'image.html', {'timelapseImage': img})
    else:
        raise Http404('Image doesn\'t exist')