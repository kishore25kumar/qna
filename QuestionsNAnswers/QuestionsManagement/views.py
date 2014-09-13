# Create your views here.
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from QuestionsManagement.models import Exam


@api_view(['POST'])
def add_question(request):
    data = request.DATA
    title = data["title"]
    start_date = data["startDate"]
    end_date = data["endData"]
    question_text = data["questionText"]
    option_a = data["optionA"]
    option_b = data["optionB"]
    option_c = data["optionC"]
    option_d = data["optionD"]
    with transaction.commit_on_success():
        exam = Exam(title=title, startDate=start_date, endDate=end_date)
        exam.save()
        question = Exam(examForeignKey=exam, questionText=question_text, optionA=option_a, optionB=option_b,
                        optionC=option_c, optionD=option_d)
        question.save()
    return Response({},200)
