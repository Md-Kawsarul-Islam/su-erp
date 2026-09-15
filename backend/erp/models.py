from django.db import models
class Department(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Semester(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=20)
    course_name = models.CharField(max_length=200)
    credit = models.DecimalField(max_digits=3, decimal_places=1)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.course_name

from django.conf import settings


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="student_profile"
    )

    student_id = models.CharField(max_length=30, unique=True)
    registration_no = models.CharField(max_length=50, unique=True)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.SET_NULL,
        null=True
    )

    session = models.CharField(max_length=20)
    batch = models.CharField(max_length=20)

    blood_group = models.CharField(
        max_length=5,
        blank=True
    )

    father_name = models.CharField(
        max_length=100,
        blank=True
    )

    mother_name = models.CharField(
        max_length=100,
        blank=True
    )

    guardian_phone = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.student_id} - {self.user.username}"

class Teacher(models.Model):
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE
    )

    teacher_id = models.CharField(
        max_length=20,
        unique=True
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    designation = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments"
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("student", "course", "semester")

    def __str__(self):
        return f"{self.student.student_id} - {self.course.course_code}"

class Attendance(models.Model):
    STATUS_CHOICES = (
        ("Present", "Present"),
        ("Absent", "Absent"),
        ("Late", "Late"),
    )

    enrollment = models.ForeignKey(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="attendances"
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="Present"
    )

    remarks = models.CharField(
        max_length=255,
        blank=True
    )

    def __str__(self):
        return f"{self.enrollment} - {self.date}"


class Result(models.Model):
    enrollment = models.OneToOneField(
        Enrollment,
        on_delete=models.CASCADE,
        related_name="result"
    )

    marks = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    grade = models.CharField(
        max_length=5
    )

    grade_point = models.DecimalField(
        max_digits=3,
        decimal_places=2
    )

    published = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f"{self.enrollment.student.student_id} - {self.grade}"



class Notice(models.Model):
    title = models.CharField(max_length=255)

    description = models.TextField()

    created_by = models.ForeignKey(
        "accounts.User",
        on_delete=models.SET_NULL,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    is_active = models.BooleanField(
        default=True
    )

    def __str__(self):
        return self.title

class Routine(models.Model):
    DAY_CHOICES = (
        ("Saturday", "Saturday"),
        ("Sunday", "Sunday"),
        ("Monday", "Monday"),
        ("Tuesday", "Tuesday"),
        ("Wednesday", "Wednesday"),
        ("Thursday", "Thursday"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    day = models.CharField(
        max_length=20,
        choices=DAY_CHOICES
    )

    start_time = models.TimeField()

    end_time = models.TimeField()

    room = models.CharField(
        max_length=50
    )

    def __str__(self):
        return f"{self.course.course_code} - {self.day}"


class ExamSchedule(models.Model):
    EXAM_TYPES = (
        ("Mid", "Mid"),
        ("Final", "Final"),
    )

    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE
    )

    semester = models.ForeignKey(
        Semester,
        on_delete=models.CASCADE
    )

    exam_type = models.CharField(
        max_length=10,
        choices=EXAM_TYPES
    )

    exam_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    room = models.CharField(
        max_length=30
    )

    def __str__(self):
        return f"{self.course.course_code} - {self.exam_type}"
