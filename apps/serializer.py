from rest_framework import serializers, viewsets
from .models import Question,Answer,UserQuezDetail

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['que_name', 'que_dis']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['ans_name', 'ans_correct', 'ans_que_id']




