from django.contrib import admin
from .models import (
    Department,
    Semester,
    Course,
    Student,
    Teacher,
    Enrollment,
    Attendance,
    Result,
    Notice,
    Routine,
    ExamSchedule,
)
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "code")
    search_fields = ("name", "code")


@admin.register(Semester)
class SemesterAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_code",
        "course_name",
        "credit",
        "department",
        "semester",
    )
    list_filter = ("department", "semester")
    search_fields = ("course_code", "course_name")


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        "student_id",
        "user",
        "department",
        "semester",
    )
    list_filter = ("department", "semester")
    search_fields = (
        "student_id",
        "user__username",
        "user__email",
    )

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = (
        "teacher_id",
        "user",
        "department",
        "designation",
    )

    search_fields = (
        "teacher_id",
        "user__username",
    )

    list_filter = (
        "department",
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
    "student",
    "course",
    "semester",
    "enrolled_at",
)

    list_filter = (
        "semester",
        "course",
    )

    search_fields = (
        "student__student_id",
        "course__course_code",
    )


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        "enrollment",
        "date",
        "status",
    )

    list_filter = (
        "status",
        "date",
    )

    search_fields = (
        "enrollment__student__student_id",
        "enrollment__course__course_code",
    )


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        "enrollment",
        "marks",
        "grade",
        "grade_point",
        "published",
    )

    list_filter = (
        "published",
        "grade",
    )

    search_fields = (
        "enrollment__student__student_id",
    )

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "created_by",
        "created_at",
        "is_active",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    search_fields = (
        "title",
    )


@admin.register(Routine)
class RoutineAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "teacher",
        "semester",
        "day",
        "start_time",
        "end_time",
        "room",
    )

    list_filter = (
        "semester",
        "day",
    )

    search_fields = (
        "course__course_code",
        "teacher__teacher_id",
    )


@admin.register(ExamSchedule)
class ExamScheduleAdmin(admin.ModelAdmin):
    list_display = (
        "course",
        "semester",
        "exam_type",
        "exam_date",
        "start_time",
        "room",
    )

    list_filter = (
        "semester",
        "exam_type",
    )

    search_fields = (
        "course__course_code",
    )


