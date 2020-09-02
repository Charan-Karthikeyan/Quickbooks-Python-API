"""
@File : app.py
@brief : Main file to call and run all the modules in the test application.
"""

from flask import Flask, request, redirect, url_for, session, g, flash, render_template
import requests
import urllib
from werkzeug.exceptions import BadRequest
from QBOService import get_companyInfo, get_InvoiceInfo, readInvoice
from utils import context, OAuth2Helper
import config
import pandas as pd 

# configuration
SECRET_KEY = 'dev key'
DEBUG = True

# setup flask
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

@app.route('/')
def index():
    """Index route"""
    return render_template(
        'index.html'
    )

"""
@brief : Funtion to get the sandbox/company information from the quickbooks database
@param : None
@return : The rendered index HTML template
"""
@app.route('/company-info')
def company_info():
    """Gets CompanyInfo of the connected QBO account"""
    request_context = context.RequestContext(session['realm_id'], session['access_token'], session['refresh_token'])
    
    response = get_companyInfo(request_context)
    if (response.status_code == 200):
        return render_template(
            'index.html',
            company_info='Company Name: ' + response.json()['CompanyInfo']['CompanyName'],
            title='QB Customer Leads',
        )
    else:
        return render_template(
            'index.html',
            company_info=response.text,
            title='QB Customer Leads',
        )

"""
@brief : Funtion to get the invoice information from the quickbooks database
@param : None
@return : The rendered index HTML template
"""
@app.route('/invoice-sess')
def getInvoice_Info():
    request_context = context.RequestContext(session['realm_id'], session['access_token'], session['refresh_token'])
    response = get_InvoiceInfo(request_context)
    # Converting the Json dict file into normal pandas dataframe format for easier reference
    output_data = pd.json_normalize(response)

    # Uncomment this line to look at all the parameters in the dataframe 
    # print(" The output frame", output_data.columns )

    final_message = ''
    for i in range(len(output_data.columns)):
        message = str(output_data[output_data.columns[i]])
        final_message = final_message + '\n' + message
    print("final_output", final_message)
    flash('Done Check print screen')
    return render_template('index.html')

"""
@brief : The authorization function to initate the process
@param : None
@return : The Url of the tool to redirect to
"""
@app.route('/auth')
def auth():
    """Initiates the Authorization flow after getting the right config value"""
    params = {
        'scope': 'com.intuit.quickbooks.accounting', 
        'redirect_uri': config.REDIRECT_URI,
        'response_type': 'code', 
        'client_id': config.CLIENT_ID,
        'state': csrf_token()
    }
    url = OAuth2Helper.get_discovery_doc()['authorization_endpoint'] + '?' + urllib.parse.urlencode(params)
    return redirect(url)

"""
@brief : Funtion to rest the Authorization keys
@param : None
@return : The redirect URL of the OAuth2 page
"""
@app.route('/reset-session')
def reset_session():
    """Resets session"""
    session.pop('qbo_token', None)
    session['is_authorized'] = False
    return redirect(request.referrer or url_for('index'))

"""
@brief : Funtion to get the call back URL
@param : None
@return : Redirect Url to the initial index template page/ the callback url
"""
@app.route('/callback')
def callback():
    """Handles callback only for OAuth2"""
    #session['realmid'] = str(request.args.get('realmId'))
    state = str(request.args.get('state'))
    error = str(request.args.get('error'))
    if error == 'access_denied':
        return redirect(index)
    if state is None:
        return BadRequest()
    elif state != csrf_token():  # validate against CSRF attacks
        return BadRequest('unauthorized')
    
    auth_code = str(request.args.get('code'))
    if auth_code is None:
        return BadRequest()
    
    bearer = OAuth2Helper.get_bearer_token(auth_code)
    realmId = str(request.args.get('realmId'))

    # update session here
    session['is_authorized'] = True 
    session['realm_id'] = realmId
    session['access_token'] = bearer['access_token']
    session['refresh_token'] = bearer['refresh_token']

    return redirect(url_for('index'))
"""
@brief : Funtion to start the session and start the server.
@param : None
@return : Token value 
"""
def csrf_token():
    token = session.get('csrfToken', None)
    if token is None:
        token = OAuth2Helper.secret_key()
        session['csrfToken'] = token
    return token

if __name__ == '__main__':
    app.run()