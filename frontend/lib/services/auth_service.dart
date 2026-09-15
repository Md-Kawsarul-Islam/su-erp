import 'dart:convert';
import 'package:http/http.dart' as http;
import '../core/api/api_endpoints.dart';
import '../core/storage/token_storage.dart';

class AuthService {
  Future<bool> login(String username, String password) async {
    try {
      final response = await http.post(
        Uri.parse(ApiEndpoints.login),
        headers: {
          'Content-Type': 'application/json',
        },
        body: jsonEncode({
          'username': username,
          'password': password,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);

        await TokenStorage.saveToken(
          data['access'],
        );

        await TokenStorage.saveRefreshToken(
          data['refresh'],
        );

        return true;
      }

      return false;
    } catch (e) {
      print("Login Error: $e");
      return false;
    }
  }

  Future<void> logout() async {
    await TokenStorage.clearTokens();
  }
}