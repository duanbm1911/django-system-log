from django.shortcuts import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from .serializers import SystemLogSerializer
from .models import SystemLogModel
from rest_framework.permissions import IsAuthenticated 
from rest_framework.parsers import JSONParser 
# Create your views here.


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated,])
def api_log_request(request):
    if request.method == 'GET':
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        start_time = request.query_params.get('start_time')
        end_time = request.query_params.get('end_time')
        device = request.query_params.get('device')
        log = request.query_params.get('log')
        model = SystemLogModel.objects.filter(date__range=[start_date,end_date], time__range=[start_time, end_time], device__contains=device , log__contains=log)
        serializer = SystemLogSerializer(model, many=True)
        data = {'message':'OK', 'data':serializer.data}
        return Response(data, status=status.HTTP_200_OK)

    else:
        request_data = request.data
        serializer = SystemLogSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            response_data = {'message':'OK', 'data': request_data}
            return Response(response_data)

# @api_view(['GET'])
# @permission_classes([IsAuthenticated,])
# def api_log_detail(request, pk):
#     try:
#         model = SystemLogModel.objects.get(pk=pk)
#     except:
#         data = {'message':'Item does not exist'}
#         return Response(data,status=status.HTTP_400_BAD_REQUEST)
#     if request.method == 'GET':
#         serializer = SystemLogSerializer(model)
#         data = {'message':'OK', 'data': serializer.data}
#         return Response(data)