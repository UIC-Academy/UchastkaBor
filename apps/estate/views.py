from django.shortcuts import render

from apps.estate.models import Estate


def home(request):
    estates = Estate.objects.all()
    image = estates[0].images.first()
    return render(request, "estate/index.html", {"estates": estates, "image": image})