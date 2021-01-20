from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework.exceptions import NotFound
from rest_framework.fields import CurrentUserDefault

from .models import Questions, QuestionResponse

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Create users
    """
    class Meta:
        model = UserModel
        fields = ['id', 'email', 'password',
                  'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True},
                        'id': {'read_only': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True}}

    def validate_password(self, value):
        try:
            validate_password(value)
        except ValidationError as exc:
            raise serializers.ValidationError(str(exc))
        return value

    def create(self, validated_data):
        user = UserModel.objects.create(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        password = validated_data['password']
        user.set_password(password)
        user.save()

        user_group = Group.objects.get(name='Users')
        user_group.user_set.add(user)
        return user


class QuestionSerializer(serializers.ModelSerializer):
    """
    Serializer for questions CRUD opertion
    """
    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'attachment_file',
                  'asked_by', 'mentor', 'is_answered']

        extra_kwargs = {'id': {'read_only': True},
                        'is_answered': {'read_only': True}}


class QuestionResponseSerializer(serializers.ModelSerializer):
    """
    Serializer for answering the questions posted by the users
    """
    class Meta:
        model = QuestionResponse
        fields = ['id', 'question', 'answer_text']

    def create(self, validated_data):
        question = validated_data['question']
        user = self.context['request'].user

        if not user == question.mentor:
            raise NotFound("This question does not belongs to you")

        question.is_answered = True
        question.save()
        return QuestionResponse.objects.create(**validated_data)


class QuestionResponseReadSerializer(serializers.ModelSerializer):
    """
    Serializer for return the list of the answered questions to the user
    """

    answer_text = serializers.RelatedField(source='Questions', read_only=True)

    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'attachment_file',
                  'asked_by', 'mentor', 'is_answered', 'answer_text']
