from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from news.models import Headline
from news.api.serializers import *



@api_view(['GET',])
def api_head(request):
    py = Headline.objects.all().order_by('-id')

    if request.method == "GET":
        serializer = HeadlineTitleSerializer(py, many=True)
        return Response(serializer.data)