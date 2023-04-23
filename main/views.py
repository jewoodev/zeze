from django.shortcuts import render
# from django.http import HttpResponse
from django.db.models import Q

from .models import Flight


# def index(request):
#     return HttpResponse("Airport Guide")


def search_flights(request):
    query = request.GET.get('q')

    if query:
        flights = Flight.objects.filter(departure_airport_icontains=query)
    else:
        flights = Flight.objects.all()

    context = {
        'flights': flights,
    }

    return render(request, 'main/search.html', context)


def result_flight_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.POST.get('kw', '').strip()
    flights = Flight.objects.order_by('date')
    if kw:
        flights = Flight.objects.filter(
            Q(destination__icontains=kw) |      # 도착지 검색
            Q(airline__icontains=kw) |          # 항공사 검색
            Q(flight_number__icontains=kw)      # 항공편 검색
        )
    return render(request, 'result.html', {'flights': flights, 'kw': kw})