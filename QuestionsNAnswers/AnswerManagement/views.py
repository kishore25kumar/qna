# Create your views here.
from datetime import datetime
from django.core.serializers import serialize
from rest_framework.decorators import api_view
from rest_framework.response import Response
from AnswerManagement.models import Result
from QuestionsManagement.models import Exam, Question, Answer


def is_valid_exam_id_now(exam_id):
    today = datetime.utcnow()
    exam = Exam(pk=exam_id)
    if not exam.startDate <= today <= exam.endDate:
        raise Exception("Invalid exam id now")

@api_view(['POST'])
def submit_answer(request):
    data = request.DATA
    exam_id = long(data["examId"])
    is_valid_exam_id_now(exam_id)
    exam = Exam.objects.get(pk=exam_id)
    question_id = long(data["questionId"])
    answer = data["answer"]
    is_right_answer = True if Answer.objects.filter(questionForeignKey=question_id, answer=answer) else False
    result = Result(userName=request.user.email, questionForeignKey=question_id, answer=answer, status=is_right_answer)
    result.save()


@api_view(['GET'])
def get_next_question(request, exam_id):
    try:
        exam_id = long(exam_id)
        is_valid_exam_id_now(exam_id)
        exam = Exam(pk=exam_id)
        all_questions = Question.objects.filter(examForeignKey=exam)
        question_ids = [question.pk for question in all_questions]
        answered_questions = Result.objects.filter(questionForeignKey__in=question_ids)
        answered_question_ids = [question.pk for question in answered_questions]
        un_answered_question_ids = list(set(question_ids)-set(answered_question_ids))
        un_answered_questions = all_questions.filter(pk__in=un_answered_question_ids)
        response_to_send = list()
        if len(un_answered_questions) != 0:
            response_to_send = serialize('json', [un_answered_questions[0],])[0]
        return Response(response_to_send, 200)
    except Exception as unknown_exception:
        return Response(str(unknown_exception), 500)
