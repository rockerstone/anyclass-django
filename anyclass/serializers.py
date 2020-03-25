from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Student, Course, Act, Timetable


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_staff']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data.get('email',  ''),
            is_staff=validated_data.get('is_staff',  False),
            is_superuser=validated_data.get('is_superuser', False)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'student_id', 'real_name', 'grade', 'college', 'major', 'student_class', 'password']
        read_only_fields = ['id', 'real_name', 'grade', 'college', 'major', 'student_class']
        extra_kwargs = {'password': {'write_only': True}}


class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['student_id', 'real_name', 'grade', 'college', 'major', 'student_class', 'password']
        extra_kwargs = {'password': {'write_only': True}}


class CourseSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'title', 'week', 'day', 'time', 'student']
        read_only_fields = ['id']


class ActSerializer(serializers.ModelSerializer):

    class Meta:
        model = Act
        fields = ['id', 'title', 'week', 'day', 'time', 'leader']
        read_only_fields = ['id']


class TimeTableSerializer(serializers.ModelSerializer):
    week = serializers.IntegerField(min_value=1, max_value=30)
    day = serializers.IntegerField(min_value=1, max_value=7)
    time = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Timetable
        fields = ['week', 'day', 'time', 'student_class', 'act']
        validators = [UniqueTogetherValidator(
            queryset=Timetable.objects.all(),
            fields=['week', 'day', 'time']
        )]
