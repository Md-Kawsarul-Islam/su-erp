import 'package:flutter/material.dart';
import '../services/auth_service.dart';

class AuthProvider extends ChangeNotifier {

  final AuthService _authService = AuthService();

  bool _loading = false;

  bool get loading => _loading;


  Future<bool> login(
      String username,
      String password
  ) async {

    _loading = true;
    notifyListeners();


    final success = await _authService.login(
        username,
        password
    );


    _loading = false;
    notifyListeners();


    return success;
  }


  Future<void> logout() async {
    await _authService.logout();
    notifyListeners();
  }

}