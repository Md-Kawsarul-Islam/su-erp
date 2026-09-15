from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    DepartmentViewSet,
    SemesterViewSet,
    CourseViewSet,
    StudentViewSet,
    TeacherViewSet,
    EnrollmentViewSet,
    AttendanceViewSet,
    ResultViewSet,
    NoticeViewSet,
    RoutineViewSet,
    ExamScheduleViewSet,
    ERPLoginView,
)


router = DefaultRouter()

router.register("departments", DepartmentViewSet)
router.register("semesters", SemesterViewSet)
router.register("courses", CourseViewSet)
router.register("students", StudentViewSet)
router.register("teachers", TeacherViewSet)
router.register("enrollments", EnrollmentViewSet)
router.register("attendance", AttendanceViewSet)
router.register("results", ResultViewSet)
router.register("notices", NoticeViewSet)
router.register("routines", RoutineViewSet)
router.register("exams", ExamScheduleViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("login/", ERPLoginView.as_view()),
]