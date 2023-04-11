from rest_framework.viewsets import ModelViewSet

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer


class QuestionViewSet(ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    filterset_fields = ['id', 'question_text', 'pub_date']


class ChoiceViewSet(ModelViewSet):
    serializer_class = ChoiceSerializer
    queryset = Choice.objects.all()
    filterset_fields = ['id', 'choice_text', 'votes']
