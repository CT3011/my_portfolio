from django.http import JsonResponse
from base.models import Questions
from .serializers import QuestionSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def votingData(request):
    questions = Questions.objects.all()

    backend = Questions.objects.filter(answer='backend').count()
    frontend = Questions.objects.filter(answer='frontend').count()
    fullstack = Questions.objects.filter(answer='fullstack').count()
    # serializer = QuestionSerializer(questions, many=True)

    return Response({'backend':backend,"frontend":frontend,'fullstack':fullstack })