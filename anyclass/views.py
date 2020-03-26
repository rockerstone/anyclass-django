import threading
from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import mixins, status
# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.exceptions import PermissionDenied, AuthenticationFailed, NotAcceptable
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .Spider.Student import FError
from .Spider.Student import Student as Spider
from .models import Student, Course, Act, Timetable
from .permissions import CreateOnly, AdminDestoryOnly
from .serializers import StudentSerializer
from .serializers import TimeTableSerializer
from .serializers import UserSerializer
from .serializers import CourseSerializer, ActSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.UpdateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated | CreateOnly]

    def create(self, request, *args, **kwargs):
        stu = {
            'username': request.data['username'],
            'stuid': request.data['username'],
            'password': request.data['password'],
        }
        try:
            spider = Spider(stu)
            info = spider.info()
            courses = spider.course()
        except FError as e:
            raise AuthenticationFailed(detail=e.__str__())
        student, created = Student.objects.get_or_create(student_id=info['student_id'])
        s = StudentSerializer(student, data=info)
        s.is_valid(raise_exception=True)
        s.save()
        Course.objects.filter(student=student).delete()
        for course in courses:
            course['student'] = student.pk
            c = CourseSerializer(data=course)
            c.is_valid(raise_exception=True)
            c.save()
        user, created = User.objects.get_or_create(username=info['student_id'])
        u = UserSerializer(user, data=stu)
        u.is_valid(raise_exception=True)
        u.save()
        return Response(u.data, status=status.HTTP_201_CREATED)

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

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff or request.user.username == instance.username:
            serializer = UserSerializer(instance)
            return Response(serializer.data)
        else:
            raise PermissionDenied()

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user.is_staff or request.user.username == instance.username:
            data = request.data.copy()
            data['is_staff'] = data.get('is_staff', False)
            if instance == request.user or not request.user.is_staff:
                data.pop('is_staff', False)
            data.pop('username', False)
            if 'password' in data and (not data['password'] or data['password'] == ''):
                data.pop('password')
            serializer = UserSerializer(instance, data=data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to
                # forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        else:
            raise PermissionDenied()


class StudentViewSet(mixins.DestroyModelMixin,
                     viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated & AdminDestoryOnly]

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
        if settings.THREAD:
            settings.THREAD = False
            create = CreateTimetable()
            create.start()
            return Response("请求已接收，请等待一分钟后查看 ^_^", status=status.HTTP_200_OK)
        else:
            raise NotAcceptable(detail="任务执行中...... >_<")

    @action(detail=False, url_path='update', url_name='update_table',
            permission_classes=[IsAdminUser])
    def update_table(self, request, *args, **kwargs):
        if settings.THREAD:
            settings.THREAD = False
            update = UpdateTimetable()
            update.start()
            return Response("请求已接收，请等待一分钟后查看 ^_^", status=status.HTTP_200_OK)
        else:
            raise NotAcceptable(detail="任务执行中...... >_<")

    def list(self, request, *args, **kwargs):
        timetable = Timetable.objects.filter(week=1)
        timetable = TimeTableSerializer(timetable, many=True)
        return Response(timetable.data)

    def retrieve(self, request, *args, **kwargs):
        timetable = Timetable.objects.filter(week=self.kwargs['week'])
        timetable = TimeTableSerializer(timetable, many=True)
        return Response(timetable.data)


class CreateTimetable(threading.Thread):
    def run(self):
        Timetable.objects.all().delete()
        timetable = []
        for week in range(1, 31):
            for day in range(1, 8):
                for time in range(1, 11):
                    data = {
                        'id': (week-1)*70+(day-1)*10+time,
                        'week': week,
                        'day': day,
                        'time': time
                    }
                    timetable.append(data)
        s = TimeTableSerializer(data=timetable, many=True)
        s.is_valid(raise_exception=True)
        s.save()
        settings.THREAD = True


class UpdateTimetable(threading.Thread):
    def run(self):
        Timetable.objects.all().update(student_class="")
        Timetable.objects.all().update(act="")

        timetable = {}
        for week in range(1, 31):
            timetable[week] = {}
            for day in range(1, 8):
                timetable[week][day] = {}
                for time in range(1, 11):
                    timetable[week][day][time] = {}

        acts = Act.objects.all()
        for act in acts:
            if 'act' not in timetable[act.week][act.day][act.time]:
                timetable[act.week][act.day][act.time]['act'] = act.title
            else:
                timetable[act.week][act.day][act.time]['act'] += (',' + act.title)

        courses = Course.objects.all()
        for course in courses:
            student_class = course.student.student_class
            weeks = course.week.split(',')
            day = int(course.day)
            times = course.time.split(',')
            for weekstr in weeks:
                week = int(weekstr)
                for timestr in times:
                    time = int(timestr)
                    if 'student_class' not in timetable[week][day][time]:
                        timetable[week][day][time]['student_class'] = student_class
                    else:
                        timetable[week][day][time]['student_class'] += (',' + student_class)

        for week in range(1, 31):
            for day in range(1, 8):
                for time in range(1, 11):
                    if 'act' in timetable[week][day][time] or 'student_class' in timetable[week][day][time]:
                        t = Timetable.objects.filter(week=week, day=day, time=time).get()
                        t.act = timetable[week][day][time].get('act', '')
                        t.student_class = timetable[week][day][time].get('student_class', '')
                        t.save()

        settings.THREAD = True
