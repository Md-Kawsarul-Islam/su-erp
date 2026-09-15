import 'package:flutter_secure_storage/flutter_secure_storage.dart';

class TokenStorage {

  static const storage = FlutterSecureStorage();


  static Future<void> saveToken(String token) async {
    await storage.write(
      key: "access_token",
      value: token,
    );
  }


  static Future<void> saveRefreshToken(String token) async {
    await storage.write(
      key: "refresh_token",
      value: token,
    );
  }


  static Future<String?> getToken() async {
    return await storage.read(
      key: "access_token",
    );
  }


  static Future<void> clearTokens() async {
    await storage.deleteAll();
  }

}