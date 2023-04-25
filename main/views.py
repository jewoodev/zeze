from django.shortcuts import render
from rest_framework.response import Response
from django.db.models import Q
from .models import Flight
from rest_framework.views import APIView
from .serializers import FlightSerializer

class FlightListAPI(APIView):
    def get(self, request):
        queryset = Flight.objects.all()
        print(queryset)
        serializer = FlightSerializer(queryset, many=True)
        return Response(serializer.data)
def search_flights(request):
    query = request.GET.get('q')
    if query:
        flights = Flight.objects.filter(departure_airport__icontains=query)
    else:
        flights = Flight.objects.all()
    context = {
        'flights': flights,
    }
    return render(request, 'main/search.html', context)


def result_flight_list(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '').strip()
    flights = Flight.objects.order_by('date')
    if kw:
        flights = Flight.objects.filter(
            Q(destination__icontains=kw) |      # 도착지 검색
            Q(airline__icontains=kw) |          # 항공사 검색
            Q(flight_number__icontains=kw)      # 항공편 검색
        )
    return render(request, 'main/result_flight_list.html', {'flights': flights, 'kw': kw})