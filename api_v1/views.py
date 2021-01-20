from django.contrib.auth import get_user_model

from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework import status, viewsets
from rest_framework.parsers import FormParser, MultiPartParser


from .serializers import UserSerializer, QuestionSerializer, QuestionResponseSerializer, \
    QuestionResponseReadSerializer
from .models import Questions, QuestionResponse
from .permissions import UserGroupPermission, MentorGroupPermission


class CreateUserAPIView(CreateAPIView):
    """
    Use this endpoint for create users
    """
    permission_classes = [permissions.AllowAny]  # Allow public users to signup
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CreateQuestionViewSet(viewsets.ModelViewSet):
    """
    Post questions by users
    """
    permission_classes = [permissions.IsAuthenticated, UserGroupPermission]
    queryset = Questions.objects.all()
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = QuestionSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(asked_by=self.request.user)
        return query_set


class QuestionsByUserListAPIView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated, UserGroupPermission]
    queryset = Questions.objects.all()
    serializer_class = QuestionResponseReadSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(is_answered=True)
        return query_set


class QuestionsListAPIView(ListAPIView):
    """
    Return the list of the questions sumbmitted by the user to mentor
    """
    permission_classes = [permissions.IsAuthenticated, MentorGroupPermission]
    serializer_class = QuestionSerializer
    model = serializer_class.Meta.model
    queryset = Questions.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(mentor=self.request.user)
        return query_set


class AnswerModelViewSet(viewsets.ModelViewSet):
    """
    Anserwing the questions asked by the users
    """
    permission_classes = [permissions.IsAuthenticated, MentorGroupPermission]
    queryset = QuestionResponse.objects.all()
    serializer_class = QuestionResponseSerializer
