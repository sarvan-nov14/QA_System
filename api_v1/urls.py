from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from .views import CreateUserAPIView, CreateQuestionViewSet, \
    QuestionsListAPIView, AnswerModelViewSet, QuestionsByUserListAPIView


router = DefaultRouter()
router.register(r'question', CreateQuestionViewSet, basename='user')
router.register(r'answer-question', AnswerModelViewSet, basename='user')

urlpatterns = [
    path('register/', CreateUserAPIView.as_view(), name='create_user'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('questions-list/', QuestionsListAPIView.as_view(), name='question_list'),
    path('answered-questions-list/',
         QuestionsByUserListAPIView.as_view(), name='question_list'),
] + router.urls
