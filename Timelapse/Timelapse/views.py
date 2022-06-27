from django.shortcuts import render
from Timelapse.models import TimelapseImage
from django.http import Http404
from django.db.models import Count


def index(request):
    dates = TimelapseImage.objects.values('date').annotate(dcount=Count('date')).order_by()
    return render(request, 'index.html', {'dates': dates})

def images(request, imagesDate):
    dates = TimelapseImage.objects.values('date').annotate(dcount=Count('date')).order_by()
    img = TimelapseImage.objects.filter(date=imagesDate)
    if img is not None:
        return render(request, 'images.html', {'timelapseImages': img, 'dates': dates})
    else:
        return render(request, 'index.html', {'dates': dates})