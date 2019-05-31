from rest_framework import viewsets
from django.contrib.auth.models import User, Group
from .serializers import TaskSerializer,Task
from rest_framework.response import Response
from django.http import JsonResponse



tasks = {"header" : {'total' : '235,890,000 RWF', 'revenue' : '178,908,788 RWF', 'growth' : '+2.0 %'}, "right":{'bon' : '128,978,000 RWF','cards' :'8,978,000 RWF', 'discounts' : '450,000 RWF', 'stock' : '128,978,000 RWF', 'cardsSold' : '450,000 RWF', 'bonSold' : '450,000 RWF', 'cardsInStock' : '8,978,000 RWF'}},
    

def getAll(req):
	return JsonResponse(tasks, safe=False)

# class TaskViewSet(viewsets.ViewSet):
#     # Required for the Browsable API renderer to have a nice form.
#     serializer_class = TaskSerializer

#     def list(self, request):
#         serializer = TaskSerializer(
#             instance=tasks.values(), many=True)
#         return Response(serializer.data)

