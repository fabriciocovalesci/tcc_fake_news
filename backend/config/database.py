import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from decouple import config



service_account = {
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


# Use a service account
cred = credentials.Certificate(service_account)
firebase_admin.initialize_app(cred)

db = firestore.client()