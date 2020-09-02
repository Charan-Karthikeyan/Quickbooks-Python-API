"""
@File : APICallService.py
@brief : Support file to call the API and communicate with them.
"""
import requests
from requests_oauthlib import OAuth1
import config
import json
"""
@brief : To send the get request to the API with the required parameters
@param : uri -> The Values of the required parameter to call from the API
         req_context ->
@return : The output from the called function from the API
NOTE : We only use this function from this file 
"""
def get_request(req_context, uri):
    """HTTP GET request for QBO API and its required API parameters"""
    headers = { 'Accept': "application/json", 
        'User-Agent': "testApp"
    }
    if config.ENVIRONMENT == "Sandbox":
        base_url = "https://sandbox-quickbooks.api.intuit.com/v3/company/"
    else:
        base_url = "https://quickbooks.api.intuit.com/v3/company/"
    url = base_url + req_context.realm_id + uri
    print(url)
    if config.AUTH_TYPE == "OAuth2":
        headers['Authorization'] = "Bearer " + req_context.access_token
        req = requests.get(url, headers=headers)
    else:
        auth = OAuth1(req_context.consumer_key, req_context.consumer_secret, req_context.access_key, req_context.access_secret)
        req = requests.get(url, auth=auth, headers=headers)
    return req
"""
@brief : To send the POSt request to the API with the required parameters
@param : uri -> The Values of the required parameter to post to the API
         req_context -> 
@return : The output from the called function from the API
"""
def post_request(req_context, uri, payload):
    """HTTP POST request for QBO API"""
    headers = { 'Accept': "application/json", 
        'content-type': "application/json; charset=utf-8", 
        'User-Agent': "testApp"
    }

    if config.ENVIRONMENT == "Sandbox":
        base_url = "https://sandbox-quickbooks.api.intuit.com/v3/company/"
    else:
        base_url = "https://quickbooks.api.intuit.com/v3/company/"
    url = base_url + req_context.realm_id + uri
    
    if config.AUTH_TYPE == "OAuth2":
        headers['Authorization'] = "Bearer " + req_context.access_token
        req = requests.post(url, headers=headers, data=json.dumps(payload))
    else:
        auth = OAuth1(req_context.consumer_key, req_context.consumer_secret, req_context.access_key, req_context.access_secret)
        req = requests.post(url, auth=auth, headers=headers, data=json.dumps(payload))
    return req




    
        
