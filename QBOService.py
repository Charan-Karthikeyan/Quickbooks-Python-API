"""
@File : QBOService.py
@brief : Functions declaration and definition that are being called from the main app.py
"""
from flask import session
from utils import context, APICallService
import json
import config
# """
# NOTE: NOT NEEDED and NOT USED
# """
# def create_customer(excel_customer, req_context):
#     """Create a customer object with customer data from a working dictionary"""
#     full_name = excel_customer['Full Name']
#     name_list = full_name.split(' ')
#     first_name = name_list[0]
#     last_name = name_list[-1]
#     if len(name_list) > 2:
#         middle_name = str(name_list[1:len(name_list) - 1])
#     else:
#         middle_name = ''
    
#     # Create customer object 
#     customer = {
#         'GivenName': first_name,
#         'MiddleName': middle_name,
#         'FamilyName': last_name,
#         'PrimaryPhone': {
#             'FreeFormNumber': excel_customer['Phone']
#         },
#         'PrimaryEmailAddr': {
#             'Address': excel_customer['Email']
#         }
#     }

#     uri = '/customer?minorversion=' + config.API_MINORVERSION
#     response = APICallService.post_request(req_context, uri, customer)
#     return response

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
    

