"""
@File : config.py
@brief : File containing the keys to the application.
"""

DEBUG = False
SQLALCHEMY_ECHO = False

# OAuth2 credentials
#Change the ID and Secret key to the given in the Keys section in the developer dashboard
CLIENT_ID= <"Enter your client ID here">
CLIENT_SECRET = <'Enter your Client sceret id here'>
# Add this url to the Add url section in the developer dashboard
REDIRECT_URI = 'http://localhost:5000/callback'

# Choose environment; default is sandbox
ENVIRONMENT = 'Sandbox'
# ENVIRONMENT = 'Production'

AUTH_TYPE ="OAuth2"
# Set to latest at the time of updating this app, can be be configured to any minor version
API_MINORVERSION = '53'

