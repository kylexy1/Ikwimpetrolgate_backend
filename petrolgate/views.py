from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from home.models import Data,Info
from .serializers import DataSerializer


@csrf_exempt
def getAll(req):
	datas = Data.objects.first()
	serializer = DataSerializer(datas, many=False)
	return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def saveFormData(request):
	i = Info(name=request.POST.get('name'), email=request.POST.get('email'), tin_number=request.POST.get('tin_number'), district=request.POST.get('district'), sector=request.POST.get('sector'), phone=request.POST.get('phone'))
	i.save()
	return JsonResponse({'message' : 'success'}, status=201)


