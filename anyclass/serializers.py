from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Student, Course, Act, Timetable


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'is_staff']
        read_only_fields = ['id']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        super().update(instance, validated_data)
        if 'password' in validated_data and validated_data['password'] != '':
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'student_id', 'real_name', 'grade', 'college', 'major', 'student_class',
                  'create_time', 'update_time']
        read_only_fields = ['id', 'create_time', 'update_time']


class CourseSerializer(serializers.ModelSerializer):
    # student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'title', 'week', 'day', 'time', 'student']
        read_only_fields = ['id']


class ActSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act
        fields = ['id', 'title', 'week', 'day', 'time', 'leader', 'description', 'create_time', 'update_time']
        read_only_fields = ['id', 'create_time', 'update_time']


class TimeTableSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    week = serializers.IntegerField(min_value=1, max_value=30)
    day = serializers.IntegerField(min_value=1, max_value=7)
    time = serializers.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Timetable
        fields = ['id', 'week', 'day', 'time', 'student_class', 'act']
        validators = [UniqueTogetherValidator(
            queryset=Timetable.objects.all(),
            fields=['week', 'day', 'time']
        )]
