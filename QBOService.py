"""
@File : QBOService.py
@brief : Functions declaration and definition that are being called from the main app.py
"""
from flask import session
from utils import context, APICallService
import json
import config

"""
@brief : Function to get the name of the sandbox that the tool is connected to
@param : The parameters of the tool
@return : The output respose from the json call. 
"""
def get_companyInfo(req_context):
    """Get CompanyInfo of connected QBO company"""
    uri = "/companyinfo/" + req_context.realm_id + "?minorversion=" + config.API_MINORVERSION
    response = APICallService.get_request(req_context, uri)
    return response

"""
@brief : Function to get the Invoice database from the Sandbox
@param : The parametes of the tool.
@return : Filtered utput from the JSON file.
"""
def get_InvoiceInfo(req_context):
    """ Getting the invoice details"""
    quer1 = 'select * from invoice'
    uri = "/query?query="+quer1+"&minorversion="+config.API_MINORVERSION
    response = APICallService.get_request(req_context,uri)
    return response.json()['QueryResponse']['Invoice']
    # return response.json()
"""
@brief : Function to read the values in the invoice 
@param : The invoice id and the parameters for the tool
@return : Outplut value from the json file.
"""
def readInvoice(req_context,invoice_id):
    # print("The invoice ID is ", invoice_id)
    uri = "/invoice/" + str(invoice_id) + "?minorversion=" + config.API_MINORVERSION
    request = APICallService.get_request(req_context,uri)
    # print("The request respose is ", request)
    return request.json()
    

