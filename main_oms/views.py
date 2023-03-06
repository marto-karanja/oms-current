from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from main_oms.models import Orders
from main_oms.serializers import TutorialSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def orders_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        orders = Orders.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            orders = orders.filter(title__icontains=title)
        
        tutorials_serializer = TutorialSerializer(orders, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        tutorial_data = JSONParser().parse(request)
        tutorial_serializer = TutorialSerializer(data=tutorial_data)
        if tutorial_serializer.is_valid():
            tutorial_serializer.save()
            return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    # find tutorial by pk (id)
    try: 
        order = Orders.objects.get(pk=pk) 
    except Orders.DoesNotExist: 
        return JsonResponse({'message': 'The order does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET': 
        tutorial_serializer = TutorialSerializer(order) 
        return JsonResponse(tutorial_serializer.data) 
 
    elif request.method == 'PUT': 
        order_data = JSONParser().parse(request) 
        tutorial_serializer = TutorialSerializer(order, data=order_data) 
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(tutorial_serializer.data) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        order.delete() 
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT) 
 
    # GET / PUT / DELETE tutorial
    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # Get all published tutorials
    orders = Orders.objects.filter(published=True)
        
    if request.method == 'GET': 
        tutorials_serializer = TutorialSerializer(orders, many=True)
        return JsonResponse(tutorials_serializer.data, safe=False)