import requests
from bs4 import BeautifulSoup


ERP_LOGIN_URL = "http://sue.su.edu.bd:5081/sonargaon_erp/"


def erp_login(username, password):

    session = requests.Session()

    try:

        # First visit (get cookies)
        session.get(ERP_LOGIN_URL)


        payload = {
            "email": username,
            "password": password,
            "login": "Login"
        }


        response = session.post(
            ERP_LOGIN_URL,
            data=payload,
            allow_redirects=True
        )


        # Debug purpose
        print(response.status_code)
        print(response.url)
        print(response.text)


        # Check login success
        if "Logout" in response.text or "Dashboard" in response.text:
            return {
                "success": True,
                "message": "Login successful"
            }


        return {
            "success": False,
            "message": "Invalid Student ID or Password"
        }


    except Exception as e:

        return {
            "success": False,
            "message": str(e)
        }