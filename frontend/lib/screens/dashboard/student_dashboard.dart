import 'package:flutter/material.dart';


class StudentDashboard extends StatelessWidget {

const StudentDashboard({super.key});


@override
Widget build(BuildContext context){

return Scaffold(

appBar: AppBar(
title:const Text(
"Student Dashboard"
),
),


body:ListView(

children:[


ListTile(
title:Text("Profile"),
),


ListTile(
title:Text("Courses"),
),


ListTile(
title:Text("Routine"),
),


ListTile(
title:Text("Attendance"),
),


ListTile(
title:Text("Result"),
),


ListTile(
title:Text("Notice"),
),


ListTile(
title:Text("Exam"),
),


],


),

);

}

}