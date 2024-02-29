from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from backend.models import *
from backend.serializers import *

from django.views.decorators.csrf import csrf_exempt

from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.
@csrf_exempt
def get_data(request):
    data = ProjectModel.objects.all().values()
    data_list = list(data)
    if request.method == 'GET':
        # serializer = ProjectModelListSerializer(data, many=True)
        return JsonResponse(data_list, safe=False)
        
