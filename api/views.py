from rest_framework.views import APIView
from rest_framework import generics, filters
from rest_framework.response import Response
from .models import Activity, Category
from .serializers import ActivitySerializer, CategorySerializer
import requests


# Create your views here.

class GenerateActivity(APIView):
    """
    View to random activity.
    """
    def get(self, format=None):
        """
        Return an activity.
        """
        new_activity = requests.get('https://www.boredapi.com/api/activity') #get request on public API
        serialized_data = ActivitySerializer(new_activity.json())
        new_category, created = Category.objects.get_or_create(name=serialized_data.data['type'])
        new_category.value = serialized_data.data['type']
        new_activity = Activity.objects.create(activity=serialized_data.data['activity'],
        type=new_category, price=serialized_data.data['price'])
        new_activity.save()
        new_category.save()
        return Response(serialized_data.data)



class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    search_fields = ['^name',]


class RetrieveActivity(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^type__name',]

class RetrieveDescendingActivity(generics.ListAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^type__name',]
    
    def get_queryset(self):
        return self.queryset.order_by('-price')