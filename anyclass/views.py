from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .Spider.Student import FError
from .Spider.Student import Student as Spider
from .models import Student, Course, Act, Timetable
from .permissions import CreateOnly, AdminDestoryOnly
from .serializers import StudentSerializer, StudentCreateSerializer
from .serializers import TimeTableSerializer
from .serializers import UserSerializer, CourseSerializer, ActSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        user = UserSerializer(user)
        return Response(user.data)

    @action(detail=False, url_path='all', url_name='list_all',
            permission_classes=[IsAdminUser])
    def list_all(self, request):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response(users.data)


class StudentViewSet(mixins.DestroyModelMixin,
                     mixins.CreateModelMixin,
                     viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [(IsAuthenticated | CreateOnly) & AdminDestoryOnly ]

    def retrieve(self, request, *args, **kwargs):
        student = get_object_or_404(Student, id=self.kwargs['pk'])
        if not request.user.is_staff and request.user.username != student.student_id:
            raise PermissionDenied()
        student = StudentSerializer(student)
        return Response(student.data)

    def list(self, request, *args, **kwargs):
        if not request.user.is_staff:
            student = Student.objects.filter(student_id=request.user.username).all()
        else:
            student = Student.objects.all()
        students = StudentSerializer(student, many=True)
        return Response(students.data)

    def create(self, request, *args, **kwargs):
        stu = {
            'username': request.data['student_id'],
            'stuid': request.data['student_id'],
            'password': request.data['password'],
        }
        try:
            spider = Spider(stu)
            info = spider.info()
            courses = spider.course()
        except FError as e:
            raise AuthenticationFailed(detail=e.__str__())
        student, created = Student.objects.get_or_create(student_id=info['student_id'])
        serializer = StudentCreateSerializer(student, data=info)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        Course.objects.filter(student=student).delete()
        # student = StudentSerializer(student)
        for course in courses:
            course['student'] = student.pk
            c = CourseSerializer(data=course)
            c.is_valid(raise_exception=True)
            c.save()

        u, created = User.objects.get_or_create(username=info['student_id'])
        u = UserSerializer(u, data=stu)
        u.is_valid(raise_exception=True)
        u.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_destroy(self, instance):
        User.objects.filter(username=instance.student_id).delete()
        instance.delete()


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if 'student' in request.query_params:
            student = get_object_or_404(Student, pk=request.query_params['student'])
            if request.user.is_staff or request.user.username == student.student_id:
                courses = Course.objects.filter(student=student).all()
            else:
                raise PermissionDenied()
        else:
            if request.user.is_staff:
                courses = Course.objects.all()
            else:
                student = get_object_or_404(Student, student_id=request.user.username)
                courses = Course.objects.filter(student=student).all()
        courses = CourseSerializer(courses, many=True)
        return Response(courses.data)


class ActViewSet(viewsets.ModelViewSet):
    queryset = Act.objects.all()
    serializer_class = ActSerializer
    permission_classes = [IsAdminUser]


class TimeTableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Timetable.objects.all()
    serializer_class = TimeTableSerializer
    lookup_field = 'week'

    @action(detail=False, url_path='create', url_name='create_table',
            permission_classes=[IsAdminUser])
    def create_table(self, request, *args, **kwargs):
        Timetable.objects.all().delete()
        for week in range(1, 31):
            for day in range(1, 8):
                for time in range(1, 11):
                    data = {
                        'week': week,
                        'day': day,
                        'time': time
                    }
                    s = TimeTableSerializer(data=data)
                    s.is_valid(raise_exception=True)
                    s.save()
        return Response("Success", status=status.HTTP_200_OK)

    @action(detail=False, url_path='update', url_name='update_table',
            permission_classes=[IsAdminUser])
    def update_table(self, request, *args, **kwargs):
        Timetable.objects.all().update(student_class="")
        Timetable.objects.all().update(act="")
        acts = Act.objects.all()
        for act in acts:
            t = Timetable.objects.filter(week=act.week, day=act.day, time=act.time).get()
            if t.act == "":
                t.act = act.title
            else:
                t.act += ',' + act.title
            t.save()
        courses = Course.objects.all()
        for course in courses:
            student_class = course.student.student_class
            weeks = course.week.split(',')
            times = course.time.split(',')
            for week in weeks:
                for time in times:
                    t = Timetable.objects.filter(week=week, day=course.day, time=time).get()
                    if t.student_class == "":
                        t.student_class = student_class
                    else:
                        scs = t.student_class.split(',')
                        if student_class not in scs:
                            t.student_class += ',' + student_class
                    t.save()
        return Response("Success", status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        timetable = Timetable.objects.filter(week=self.kwargs['week'])
        timetable = TimeTableSerializer(timetable, many=True)
        return Response(timetable.data)
