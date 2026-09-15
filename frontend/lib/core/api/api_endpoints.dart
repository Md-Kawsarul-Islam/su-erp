class ApiEndpoints {
  static const String baseUrl = String.fromEnvironment(
    'API_BASE_URL',
    defaultValue: 'http://localhost:8000',
  );

  static const String login = "$baseUrl/api/token/";

  static const profile = "/accounts/profile/";

  static const departments = "/erp/departments/";
  static const semesters = "/erp/semesters/";
  static const courses = "/erp/courses/";
  static const students = "/erp/students/";
  static const teachers = "/erp/teachers/";
  static const enrollments = "/erp/enrollments/";
  static const attendance = "/erp/attendance/";
  static const results = "/erp/results/";
  static const routines = "/erp/routines/";
  static const notices = "/erp/notices/";
  static const exams = "/erp/exams/";
}
