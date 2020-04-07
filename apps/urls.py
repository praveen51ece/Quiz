from django.contrib import admin
from django.urls import path
from apps import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('api/question', views.QuestionList.as_view()),
    path('api/answer', views.AnswerList.as_view()),
]
