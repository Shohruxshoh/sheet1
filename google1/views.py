from django.shortcuts import redirect
from django.http import HttpResponse
from google.auth.transport import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from django.conf import settings


# Create your views here.


def google_auth(request):
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
                "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                "redirect_uris": "http://127.0.0.1:8000/auth/google/callback",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "scopes": settings.GOOGLE_OAUTH2_SCOPE,
            }
        },
        scopes=settings.GOOGLE_OAUTH2_SCOPE,
    )
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
    )
    # print(authorization_url)
    return redirect(authorization_url)


def google_auth_callback(request):
    print("jjjjjjjjjjjjj")
    flow = Flow.from_client_config(
        {
            "web": {
                "client_id": settings.GOOGLE_OAUTH2_CLIENT_ID,
                "client_secret": settings.GOOGLE_OAUTH2_CLIENT_SECRET,
                "redirect_uris": "http://127.0.0.1:8000/auth/google/callback",
                "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                "token_uri": "https://accounts.google.com/o/oauth2/token",
                "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                "scopes": settings.GOOGLE_OAUTH2_SCOPE,
            }
        },
        scopes=settings.GOOGLE_OAUTH2_SCOPE,
    )
    flow.fetch_token(authorization_response=request.get_full_path())
    credentials = flow.credentials

    # Faylarni o'qish uchun foydalanuvchi autentifikatsiya ma'lumotlarini saqlang
    request.session['google_credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    return redirect('api/')  # Asosiy sahifaga qaytish
