import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import '../../providers/auth_provider.dart';
import '../dashboard/student_dashboard.dart';


class LoginScreen extends StatefulWidget {

  const LoginScreen({super.key});


  @override
  State<LoginScreen> createState() =>
      _LoginScreenState();

}



class _LoginScreenState extends State<LoginScreen>{

  final usernameController =
      TextEditingController();

  final passwordController =
      TextEditingController();



  void login() async {


    final auth =
    Provider.of<AuthProvider>(
        context,
        listen:false
    );


    bool success =
    await auth.login(
        usernameController.text,
        passwordController.text
    );


    if(success){

      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder:(context)=>
          const StudentDashboard(),
        ),
      );

    }
    else{

      ScaffoldMessenger.of(context)
          .showSnackBar(
        const SnackBar(
          content:
          Text("Invalid username or password"),
        ),
      );

    }

  }



  @override
  Widget build(BuildContext context){

    return Scaffold(

      appBar: AppBar(
        title:
        const Text("Student ERP Login"),
      ),


      body: Padding(

        padding:
        const EdgeInsets.all(20),


        child: Column(

          mainAxisAlignment:
          MainAxisAlignment.center,


          children:[


            TextField(

              controller:
              usernameController,

              decoration:
              const InputDecoration(
                labelText:"Username",
              ),

            ),



            TextField(

              controller:
              passwordController,

              obscureText:true,

              decoration:
              const InputDecoration(
                labelText:"Password",
              ),

            ),



            const SizedBox(height:30),



            Consumer<AuthProvider>(

              builder:(context,auth,child){


                return ElevatedButton(

                  onPressed:
                  auth.loading
                      ? null
                      : login,


                  child:
                  auth.loading

                      ? const CircularProgressIndicator()

                      : const Text("Login"),

                );

              },

            )

          ],

        ),

      ),

    );

  }

}