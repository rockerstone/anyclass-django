from django.db import models


# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=255, default='')
    real_name = models.CharField(max_length=20, default='')
    grade = models.IntegerField(default=0)
    college = models.CharField(max_length=100, default='')
    major = models.CharField(max_length=100, default='')
    student_class = models.CharField(max_length=100, default='')

    def __str__(self):
        return "%s %s" % (self.real_name, self.student_id)


class Course(models.Model):
    title = models.CharField(max_length=100)
    week = models.CharField(max_length=255, default='')
    day = models.CharField(max_length=255, default='')
    time = models.CharField(max_length=255, default='')
    student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Act(models.Model):
    title = models.CharField(max_length=100, unique=True)
    week = models.CharField(max_length=255, default='')
    day = models.CharField(max_length=255, default='')
    time = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=255, default='')
    leader = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Timetable(models.Model):
    week = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    time = models.IntegerField(default=0)
    student_class = models.CharField(max_length=255, default="")
    act = models.CharField(max_length=255, default="")

    def __str__(self):
        return "%d %d %d" % (self.week, self.day, self.time)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['week', 'day', 'time'], name="unique_time")]
