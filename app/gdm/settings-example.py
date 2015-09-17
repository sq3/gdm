# Copy your credentials from the console
CLIENT_ID_SRC = '1234567890abcdefg.apps.googleusercontent.com'
CLIENT_SECRET_SRC = '1a2b3c4f-ABCDEDF-ABC'

"""Email of the Service Account"""
SERVICE_ACCOUNT_DST = '123456789-abcdefg@developer.gserviceaccount.com'

"""Path to the Service Account's Private Key file"""
SERVICE_ACCOUNT_PRIVATE_KEY_DST = './dst-gdrive.p12'

# Check https://developers.google.com/drive/scopes for all available scopes
OAUTH_SCOPE = 'https://www.googleapis.com/auth/drive'

# Redirect URI for installed apps
REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'
