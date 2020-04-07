from django.shortcuts import render
from rest_framework import generics
from .models import Question,Answer,UserQuezDetail
from .serializer import QuestionSerializer,AnswerSerializer

def home(request):
	if request.POST:
		que_id = request.POST.get('que_id')
		que_ans_id = request.POST.get('ans_id')
		User_ans = UserQuezDetail()
		User_ans.qz_user = request.user
		User_ans.qz_que_name = que_id
		User_ans.qz_ans_name =que_ans_id
		User_ans.save()
		return render(request,'home/result_page.html',dict_data)

	else:
		questions = Question.objects.all()
		for question in questions:
			question.answers = Answer.objects.filter(ans_que_id=question.pk)
		dict_data = {'questions':questions, 'user':request.user}
		return render(request,'home/home.html',dict_data)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class AnswerList(generics.ListCreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
