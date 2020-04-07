from django.db import models

# Create your models here.

class Question(models.Model):
	que_name = models.CharField(max_length=400, null=False)
	que_dis = models.CharField(max_length=500, null=False)

	def __str__(self):
		return self.que_name

class Answer(models.Model):
	ans_name = models.CharField(max_length=100, null=False)
	ans_correct = models.IntegerField(default=0 ,null=False)
	ans_que_id = models.IntegerField(null=False)

	def __str__(self):
		return self.ans_name

class UserQuezDetail(models.Model):
	qz_user = models.CharField(max_length = 50,null=False)
	qz_que_name = models.CharField(max_length=400, null=False)
	qz_ans_name = models.CharField(max_length=100,null=False)

	def __str__(self):
		return self.qz_user