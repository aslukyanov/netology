from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv

def index(request):
    return redirect(reverse('bus_stations'))


STATIONS_LIST = []
with open('data-398-2018-08-30.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader :
        STATIONS_LIST.append(row)


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(STATIONS_LIST, 10)
    page = paginator.get_page(page_number)
    # print(f"PAGE NUMBER IS {page_number}")
    context = {
        'bus_stations': STATIONS_LIST[(page_number - 1) * 10:page_number * 10],
        'page': page,
    }

    return render(request, 'stations/index.html', context)
