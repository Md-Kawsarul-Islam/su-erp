import 'package:dio/dio.dart';
import 'api_endpoints.dart';
import '../storage/token_storage.dart';


class ApiClient {

  final Dio dio = Dio(
    BaseOptions(
      baseUrl: ApiEndpoints.baseUrl,
      connectTimeout: const Duration(seconds: 10),
      receiveTimeout: const Duration(seconds: 10),
      headers: {
        "Content-Type": "application/json",
      },
    ),
  );


  ApiClient(){

    dio.interceptors.add(
      InterceptorsWrapper(

        onRequest: (options, handler) async {

          final token = await TokenStorage.getAccessToken();

          if(token != null){
            options.headers["Authorization"] =
                "Bearer $token";
          }

          return handler.next(options);
        },


        onError: (error, handler){

          print(
            "API Error: ${error.response?.data}"
          );

          return handler.next(error);

        }

      ),
    );

  }

}