import factory
from .models import Question

class QuestionFactiory(factory.django.DjangoModelFactory):
    class Meta:
        model = Question

    question_text = factory.Faker('text', max_nb_chars=100)
    pub_date = factory.Faker('date')
