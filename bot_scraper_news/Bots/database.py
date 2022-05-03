import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from decouple import config


config_firebase = {
      "type": config("TYPE"),
      "project_id": config("PROJECT_ID"),
      "private_key_id": config("PRIVATE_KEY_ID"),
      "private_key": config("PRIVATE_KEY").replace('\\n', '\n'),
      "client_email": config("CLIENT_EMAIL"),
      "client_id": config("CLIENT_ID"),
      "auth_uri": config("AUTH_URI"),
      "token_uri": config("TOKEN_URI"),
      "auth_provider_x509_cert_url": config("AUTH_PROVIDER_X_CERT_URL"),
      "client_x509_cert_url": config("CLIENT_X_CERT_URL"),
      }


class DataBase:
    
    def __init__(self):
        self.credentials = credentials.Certificate(config_firebase)
        self.init = firebase_admin.initialize_app(self.credentials)
        self.data_base = firestore.client()
